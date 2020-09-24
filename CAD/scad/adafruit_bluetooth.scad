$fn=200;

length = 26.5;
width= 23.5;
height = 6;
corner = 1;


// FRONT (logo)
translate([width+10, 0, 0]){ 
        front();
        //translate([13,14,0]) bluetooth();
}

// BACK (pins)
difference(){
    back();
    pins();
}

module back(){  
    translate([1,0,0])
    difference() {
          roundedBox(length+4, width+4, height, corner); 
          translate([1,1,1])
          roundedBox(length+2, width+2, height-1, corner); 
        }
}

module front(){
           roundedBox(length+4, width+4, 1, corner);
            difference() {
                translate([1,1,0]) {
                    roundedBox(length+2,width+2,4,corner);
                }
                translate([2,2,0]) {
                    roundedBox(length,width,4,corner);
                }              
        };            
}

module pins(){
    translate([2,2,0])
    cube([width,3.5,3]);
}

// TODO: import bluetooth logo
/*
module bluetooth(){
    scale([.45,.45,1])
    linear_extrude(height = 1.5, center = true, convexity = 10)
    //import file here
}
*/

module roundedBox(length, width, height, radius)
{
    diameter = 2*radius;
    //base rounded shape
    minkowski() {
        cube(size=[width-diameter,length-diameter, height]);
        cylinder(r=radius, h=0.01);
    } 
}
