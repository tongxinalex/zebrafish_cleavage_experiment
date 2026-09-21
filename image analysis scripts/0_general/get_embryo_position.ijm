//directory = "H:/Xin home drive/RAW DATA/Nikon CSU1/xin250312_csu2_test_micropipette/";
//directory = "H:/Xin home drive/data_meroblastic/Laser_cutter/laser_cutter_ii/xin250401_lcii_wt/";
directory = "H:/Xin home drive/RAW DATA/Nikon CSU1/xin250401_lcii_wt/";
//directory = getDirectory("Test directory");
files = getFileList(directory);

function range(x1, x2){
	list_range = newArray(x1, x2);
	list_length = list_range[1] - list_range[0];
	list = newArray(list_length);
	
	for (i=0; i<list_length; i++){
		list[i] = list_range[0] + i;
	}
	return list;
}

for (i=0; i<files.length; i++){
	file_name = files[i];
	if (indexOf(file_name, ".nd2") >= 0){
		file_position = directory + file_name;
//		print(file_position);
		run("Bio-Formats", "open=[" + file_position + "] color_mode=Default rois_import=[ROI manager] view=Hyperstack stack_order=XYCZT use_virtual_stack");
//		run("Bio-Formats", "open=[" + file_position + "] color_mode=Default display_metadata rois_import=[ROI manager] view=Hyperstack stack_order=XYCZT");
		x_pos = getInfo("m_dXYPositionX0");
		y_pos = getInfo("m_dXYPositionY0");
		print(file_name + ',' + x_pos + ',' + y_pos);
		close("*");
	}
}

selectWindow("Log");
saveAs("Text", directory + "embryo_positions.csv");
print("Awesome! Done");








// version 2 

//function range(x1, x2){
//	list_range = newArray(x1, x2);
//	list_length = list_range[1] - list_range[0];
//	list = newArray(list_length);
//	
//	for (i=0; i<list_length; i++){
//		list[i] = list_range[0] + i;
//	}
//	return list;
//}
//
////directory = "H:/Xin home drive/RAW DATA/Nikon CSU1/xin250312_csu2_test_micropipette/";
////directory = "X:/Xin home drive/data_meroblastic/Laser_cutter/laser_cutter_ii/xin250328_lcii_wt_40x/";
//directory = "H:/Xin home drive/RAW DATA/Nikon CSU1/xin250403_lcii_wt/";
////directory = getDirectory("Test directory");
//
//files = range(1, 65);
//
//for (i=0; i<files.length; i++){
//	file_name = files[i];
//	file_position = directory + file_name + ".tif";
//	run("Bio-Formats", "open=[" + file_position + "] color_mode=Default rois_import=[ROI manager] view=Hyperstack stack_order=XYCZT use_virtual_stack");
////		run("Bio-Formats", "open=[" + file_position + "] color_mode=Default display_metadata rois_import=[ROI manager] view=Hyperstack stack_order=XYCZT");
//	x_pos = getInfo("m_dXYPositionX0");
//	y_pos = getInfo("m_dXYPositionY0");
//	print(file_name + ',' + x_pos + ',' + y_pos);
//	close("*");
//}
//
//selectWindow("Log");
//saveAs("Text", directory + "embryo_positions.csv");
//print("Awesome! Done");


