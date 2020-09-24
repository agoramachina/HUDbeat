$fn=200;

length = 28;
width= 33;
height = 6;
corner = 1;

difference(){ 
    back();
    windowPins();
}

difference(){
    case();
    windowScreen();
}

module back(){   
    difference() {
                roundedBox(length+4, width+4, height, corner); 
                translate([1,1,1]) {
                    roundedBox(length+2, width+2, height-1, corner); 
                }
        }
}

module windowPins(){
    translate([2,2,0]){
    cube([width-3 , 4, 1]);}
}

module case(){
    translate([width+10, 0, 0]){     
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
}

module windowScreen(){
    translate([width+13, 5.5, 0]){  
    cube([width-3.5,16,2]);}   
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