$fn = 100;
difference() {
	hull() {
		translate([0, 0, 140]) {
			rotate([-10, 0, 0]) {
				cube([180, 235, 10]);
			}
		}
		cube([180, 8, 149]);
	}
	translate([20, 0, 0]) {
		rotate([-10, 0, 0]) {
			translate([0, -100, 0]) {
				cube([140, 335, 140]);
			}
		}
	}
	mirror([0, 1, 0]) {
		rotate([90, 0, 0]) {
			translate([10, 40, 0]) {
				cylinder(7.25, d1=7, d2=7);
				translate([0, 0, 7.25]) {
					cylinder(1000, d1=16, d2=16);
				}
				translate([0, 100, 0]) {
					cylinder(7.25, d1=7, d2=7);
					translate([0, 0, 7.25]) {
						cylinder(1000, d1=16, d2=16);
					}
				}
				translate([160, 0, 0]) {
					cylinder(7.25, d1=7, d2=7);
					translate([0, 0, 7.25]) {
						cylinder(1000, d1=16, d2=16);
					}
					translate([0, 100, 0]) {
						cylinder(7.25, d1=7, d2=7);
						translate([0, 0, 7.25]) {
							cylinder(1000, d1=16, d2=16);
						}
					}
				}
			}
		}
	}
}
