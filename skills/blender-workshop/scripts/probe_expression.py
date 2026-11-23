"""Measure a wink and a smile/squint combination on original abstract lid ribbons.

Run with an empty standalone bpy Python (Blender 4.5 LTS). No keyframes,
render, external asset or output file. All measurements are of evaluated mesh
positions, not requested slider values. The rig is a diagnostic, not an avatar.
"""
import json


def main():
    import bpy

    if not bpy.app.background or bpy.data.filepath:
        raise RuntimeError('Use a separate background Python without an open file.')
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    controls = bpy.data.objects.new('Original expression controls', None)
    scene.collection.objects.link(controls)
    for name in ('Smile', 'Squint', 'Wink'):
        controls[name] = 0.0
    points, faces, spans = [], [], {}
    samples = (-1.0, -.5, 0.0, .5, 1.0)
    profile = [1.0 - .65 * t * t for t in samples]
    for side, center in [('L', .031), ('R', -.031)]:
        for lid, base, outer in [('upper', .006, .0015), ('lower', -.004, -.0015)]:
            rows = []
            for depth in (0., outer):
                start = len(points)
                rows.append(list(range(start, start + len(samples))))
                points.extend((center + t * .014, .002 * t * t, base * weight + depth)
                              for t, weight in zip(samples, profile))
            spans[side, lid] = rows
            for a,b,c,d in zip(rows[0], rows[0][1:], rows[1][1:], rows[1]):
                faces.append((a,b,c,d))
    mesh = bpy.data.meshes.new('Abstract paired lid ribbons')
    mesh.from_pydata(points, [], faces); mesh.update()
    rig = bpy.data.objects.new('Lid aperture fixture', mesh)
    scene.collection.objects.link(rig)
    rig.shape_key_add(name='Basis', from_mix=False)

    def lift(key, lid, distance):
        for row in spans['L', lid]:
            for idx, weight in zip(row, profile):
                key.data[idx].co.z += distance * weight

    def driven(key, pairs, expression):
        driver = key.driver_add('value').driver
        driver.type = 'SCRIPTED'
        for variable, prop in pairs:
            var = driver.variables.new(); var.name = variable; var.type = 'SINGLE_PROP'
            var.targets[0].id = controls; var.targets[0].data_path = f'["{prop}"]'
        driver.expression = expression

    def pose(smile=0., squint=0., wink=0.):
        for key, value in zip(('Smile', 'Squint', 'Wink'), (smile, squint, wink)):
            controls[key] = float(value)
        controls.update_tag(); bpy.context.view_layer.update()
        evaluated = rig.evaluated_get(bpy.context.evaluated_depsgraph_get())
        return [v.co.copy() for v in evaluated.data.vertices]

    def gaps(p, side):
        return [(p[a].z - p[b].z) * 1000 for a, b in zip(spans[side, 'upper'][0], spans[side, 'lower'][0])]

    def drift(a, b, ids):
        return max((a[i] - b[i]).length * 1000 for i in ids)

    for name, shifts in [('Smile', (0., .004)), ('Squint', (-.007, 0.)), ('Wink', (-.007, .003))]:
        key = rig.shape_key_add(name=name + '.L', from_mix=False)
        for lid, distance in zip(('upper', 'lower'), shifts):
            lift(key, lid, distance)
        driven(key, [('v', name)], 'v')

    neutral = pose(); smile = pose(smile=1); squint = pose(squint=1); crossed = pose(1,1)
    # Capture the *uncorrected* combined shape. Relative to this reference,
    # the next key adds a local residual only; the reference has zero weight.
    reference = rig.shape_key_add(name='Reference: full mix', from_mix=True)
    corrected = rig.shape_key_add(name='Residual: crowding', from_mix=True)
    corrected.relative_key = reference
    lift(corrected, 'upper', .002)
    driven(corrected, [('a', 'Smile'), ('b', 'Squint')], 'a*b')
    corrected_full = pose(1,1); left_wink = pose(wink=1)
    grid = [pose(a, b) for a in (0., .25, .5, .75, 1.) for b in (0., .25, .5, .75, 1.)]
    right = [i for lid in ('upper', 'lower') for row in spans['R', lid] for i in row]
    all_indices = range(len(points))
    result = {
        'runtime': bpy.app.version_string,
        'uncorrected_combo_center_mm': gaps(crossed, 'L')[2],
        'corrected_combo_center_mm': gaps(corrected_full, 'L')[2],
        'smallest_corrected_gap_mm': min(min(gaps(p, 'L')) for p in grid),
        'solo_control_change_mm': max(drift(old, pose(*mix), all_indices) for old, mix in
                                      [(neutral, (0.,0.)), (smile, (1.,0.)), (squint, (0.,1.))]),
        'right_rim_drift_mm': max(drift(neutral, p, right) for p in [*grid, left_wink]),
        'wink_max_gap_mm': max(map(abs, gaps(left_wink, 'L'))),
        'right_open_gap_at_wink_mm': gaps(left_wink, 'R')[2],
        'static_combinations': len(grid),
    }
    assert result['uncorrected_combo_center_mm'] < 0 < result['smallest_corrected_gap_mm'], result
    assert result['wink_max_gap_mm'] < .001 and result['right_rim_drift_mm'] < .001, result
    assert result['solo_control_change_mm'] < .001 and result['right_open_gap_at_wink_mm'] > 5, result
    print('LID_PROBE ' + json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
