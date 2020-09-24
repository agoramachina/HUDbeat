$fn=200;

length = 27;
width= 15;
height = 7.7;
corner = 1;

// BACK
translate([width+10, 0, 0]){ 
    difference(){
        back();
        translate([.5,0,1]) port();
        translate([-18,0,-1.5]) sd();
        translate([0,-1,1]) camera();
        //translate([width,2,1]) mic();
        //translate([width-5,-1,1]) mic();
    }
    translate([-1,7,.5]) cube([1,13,2]); //sd buffer
    //translate([5,length+2,1]) cube([7,1,1]); //camera buffer
    //translate([17,1,1]) cube([1,6,1]); //mic buffer
    //translate([13,0,1]) cube([5,1,1]); //mic buffer
}

// CASE
difference(){
    case();
    translate([1.5,0,3]) port();
    translate([0,3,3]) mic();
    translate([-1,0,2]) sd();
    
}

module case(){  
    translate([1,0,0])
    difference() {
        roundedBox(length+4, width+4, height, corner); 
        union(){
            translate([1,1,1]) 
            roundedBox(length+2, width+2, height-1, corner); 
            translate([0,0,1]) camera();
        }    
    }
}

module back(){
           roundedBox(length+4, width+4, 1, corner);
            difference() {
                translate([1,1,0]) {
                    roundedBox(length+2,width+2,4,corner);
                }
                translate([2,2,0]) {
                    roundedBox(length,width,4,corner);
                }              
        }            
}

module port(){
    translate([4,-1,-1])
    cube([8,5,7]);
}

module camera(){
    translate([5,length+2,1])
    cube([7,2,6]);
}
module mic(){
    rotate([90,0,90]) cylinder(r=2,h=2);
}

module sd(){
    translate([width+2,7,4])
    cube([3,13,4]);
}

module roundedBox(length, width, height, radius)
{
    diameter = 2*radius;
    //base rounded shape
    minkowski() {
        cube(size=[width-diameter,length-diameter, height]);
        cylinder(r=radius, h=0.01);
    } 
}
