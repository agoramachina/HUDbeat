$fn=200;

length = 36;
width= 18;
height = 9.6;
corner = 1;


// CASE
translate([width+12, 0, 0]){
difference(){
    case();
    usb();
    reset();
    led();
    }
}

// LID
difference(){
    lid();
    translate([0,0,height-6]) usb();  
} 

module lid(){  
    difference() {
        roundedBox(length+4, width+4, height, corner); 
        translate([1,1,1]) 
            roundedBox(length+2, width+2, height-1, corner); 
        }
}

module case(){    
       roundedBox(length+4, width+4, 1, corner);
        difference() {
            translate([1,1,0]) 
                roundedBox(length+2,width+2,5,corner);
            translate([2,2,0]) 
                roundedBox(length,width,5,corner);
        }            
}

module usb(){
    translate([6,-2,0]) cube([8,9,7]);
}

module led(){
    //translate([13,12,0]) cube([2,2,2]); //square
    translate([6,13,0]) cylinder(r=1.25, h=3); //circle

    }
  
module reset(){
    //translate([width/2-.5, length-6,-1]) cube([3,3,3]); //square
    translate([width/2+1, length-4.5,0]) cylinder(r=1.75,h=3); //circle

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
