getDimensions(width, height, channels, slices, frames);
getVoxelSize(width_pixel_size, height_pixel_size, depth_size, unit);
window_name = getTitle();

Dialog.create("How to resize?");
Dialog.addChoice("Stretch or compress?", newArray("Stretch", "Compress"), "Stretch");
Dialog.show();
up_or_down = Dialog.getChoice();

Dialog.create("Interpolation?");
Dialog.addChoice("Interpolation:", newArray("None", "Bilinear", "Bicubic"), "Bicubic");
Dialog.show();
interpolation = Dialog.getChoice();

if (up_or_down == "Stretch"){
	if(height_pixel_size > width_pixel_size){  
		print("Stretching on Y-axis");
		ratio = height_pixel_size / width_pixel_size;
		print("The scalar is: " + ratio);
		run("Scale...", "x=1.0 y="+ratio+" z=1.0 interpolation="+interpolation+" average process create title=["+window_name+"_stretched]");
	}
	else {
		print("Stretching on X-axis");
		ratio = width_pixel_size / height_pixel_size;
		print("The scalar is: " + ratio);
		run("Scale...", "x="+ratio+" y=1.0 z=1.0 interpolation="+interpolation+" average process create title=["+window_name+"_stretched]");
	}
} else if (up_or_down == "Compress"){
	if(height_pixel_size > width_pixel_size){
		print("Compressing on X-axis");
		ratio = width_pixel_size / height_pixel_size;
		print("The scalar is: " + ratio);
		run("Scale...", "x="+ratio+" y=1.0 z=1.0 interpolation="+interpolation+" average process create title=["+window_name+"_stretched]");
	}
	else {
		print("Compressing on Y-axis");
		ratio = width_pixel_size / height_pixel_size;
		print("The scalar is: " + ratio);
		run("Scale...", "x=1.0 y="+ratio+" z=1.0 interpolation="+interpolation+" average process create title=["+window_name+"_stretched]");
	}
}
