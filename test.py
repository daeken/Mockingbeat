from mockingbeat import *
from math import *

"""with difference:
	cube([100, 100, 100])

	cube[right(50), up(25), forward(25)]([200, 200, 200])

	with translate([-10, 50, 60]):
		cube(200)"""

"""def foo():
	for i in xrange(600 - 1):
		sv = i / 600.
		sv = 1 - sv ** 2
		with scale([sv, sv, 1]):
			def temp(i):
				i /= 4.
				with rotate([0, 0, i * 2]):
					with translate([2.5 * sin(i / 20.), 2.5 * sin(i / 3.), i * 2]):
						with rotate([0, 0, i * 2]):
							cube([25, 25, 0.01])
			with hull:
				temp(i)
				temp(i + 1)
				temp(i + 2)

with scale([2, 2, 1]):
	for i in xrange(0, 360, 120):
		with rotate([0, 0, i]):
			foo()
			with mirror([0, 1, 0]):
				foo()
"""

fn(100)

platform_angle = 10
platform_width = 180
platform_length = 235
platform_thickness = 10

arm_width = 20
arm_length = 140
arm_thickness = 8

upper_hole_diameter = 16
lower_hole_diameter = 7
lower_hole_thickness = 7.25

with difference:
	with hull:
		with translate([0, 0, arm_length]):
			with rotate([-platform_angle, 0, 0]):
				cube([platform_width, platform_length, platform_thickness])
		cube([platform_width, arm_thickness, arm_length + 9])
	with translate([arm_width, 0, 0]):
		with rotate([-platform_angle, 0, 0]):
			with translate([0, -100, 0]):
				cube([platform_width - arm_width * 2, platform_length + 100, arm_length])
	with mirror([0, 1, 0]):
		with rotate([90, 0, 0]):
			with translate([arm_width / 2, 40, 0]):
				cylinder(lower_hole_thickness, lower_hole_diameter, lower_hole_diameter)
				with translate([0, 0, lower_hole_thickness]):
					cylinder(1000, upper_hole_diameter, upper_hole_diameter)
				with translate([0, 100, 0]):
					cylinder(lower_hole_thickness, lower_hole_diameter, lower_hole_diameter)
					with translate([0, 0, lower_hole_thickness]):
						cylinder(1000, upper_hole_diameter, upper_hole_diameter)
				with translate([160, 0, 0]):
					cylinder(lower_hole_thickness, lower_hole_diameter, lower_hole_diameter)
					with translate([0, 0, lower_hole_thickness]):
						cylinder(1000, upper_hole_diameter, upper_hole_diameter)
					with translate([0, 100, 0]):
						cylinder(lower_hole_thickness, lower_hole_diameter, lower_hole_diameter)
						with translate([0, 0, lower_hole_thickness]):
							cylinder(1000, upper_hole_diameter, upper_hole_diameter)

"""with difference:
	with union:
		cylinder[up(10)](2, 14, 14)
		cylinder(10, 6.25, 6.25)
	cylinder[down(5)](20, 5, 5)
"""
