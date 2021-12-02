import bpy
from mathutils import Vector
context = bpy.context
# parameters
cr = 1 # corner radus
L = 4  # initial width
dL = -0.25 # shrink (grow -ve) factor
turns = 10 # number of turns in spiral

def add_bezier(pts):
    curve = bpy.data.curves.new('Curve', 'CURVE')
    spline = curve.splines.new('BEZIER')

    spline.bezier_points.add(count=len(pts) - 1)
    spline.bezier_points.foreach_set("co", [c for p in pts for c in p])
    x = cr * Vector((1, 0, 0))
    y = cr * Vector((0, 1, 0))
    lhs = (y, -x, -x, -y, -y, x, x, y)
    spline.bezier_points.foreach_set("handle_left", [c  for i,p in enumerate(pts) for c in p + lhs[i%8]])
    spline.bezier_points.foreach_set("handle_right", [c for p in pts for c in p])

    ob = bpy.data.objects.new('Curve', curve)
    spline.bezier_points[0].select_control_point = True
    return ob

corners = []
loc = Vector((-L / 2, -L / 2, 0))
for turn in range(turns):
    for sy in (1, -1):
        for sx in (sy, -sy):
            v = (sx * L, 0, 0) if sx == sy else (0, sy * L, 0)

            cverts = ((cr * sx, 0, 0), (0, cr * sy, 0))
            if sx == sy: cverts = reversed(cverts)
            corners.append([loc + Vector(p) for p in cverts])
            loc = loc + Vector(v)
        L -= dL

scene = context.scene   

pts = []  
for p in corners:
    pts.extend(p)
#scene.objects.link(add_bezier(pts))