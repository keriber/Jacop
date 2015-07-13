macro "Repeat_Jacop"{

dir = getDirectory("Select Directory with Images");
dir2= getDirectory("Select Directory to save log files");

red_file = "masked_red.tif";
green_file = "masked_green.tif";

//dir2= makeDirectory(dir+'\\Log_Files');

list = getFileList(dir);
array1= newArray(list.length);
for (i=0; i <list.length;i++){
    if ( File.isDirectory(dir+list[i]))
    //if (endsWith(list[i], ".zip"))
       {imgName =list[i];
       //print(imgName);
      //write(imgName);
       //Array.show(list);
       //array[i]
       open(dir+list[i]+red_file);
       setAutoThreshold();
	   getThreshold(lowera,uppera);
	   lowera = d2s(lowera, 0);
	   open(dir+list[i]+green_file);
	   setAutoThreshold();
	   getThreshold(lowerb,upperb);
	   lowerb = d2s(lowerb, 0);
	   string = "imga=" + red_file + " imgb="+ green_file+ " thra="+lowera+" thrb="+lowerb + " pearson overlap mm ccf=20 cytofluo ica";
       
       run("JACoP ", string);
       run("Close All");
       selectWindow("Log");
       imgName =  substring(imgName, 0,  lengthOf(imgName)-1);
       saveAs("text", dir2+imgName+"_Log.txt");
       selectWindow("Log");
       run("Close");
       }
}

