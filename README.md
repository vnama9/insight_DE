# insight_DE
Data Engineer Challenge

This is done using Alteryx platform for the efficient way to make the process run faster for scalable data

We need Alteryx 11.0 or higher version to run the workflow

Workflow is found in scr_alteryx_workflow as Insight_DE.yxzp file 

Input
. Input contains input example file itcont.txt

percentile
.Percentile value is found in the percentile.txt

Output
. Output contains output text document for the input itcont.txt

Workflow:
1.Workflow has to be imported and once done you find the alteryx workflow
2.Change the input by clicking the input on the workflow on the canvas and you get the option towards right 
  to browse and uncheck the first field contains header as our input don't contain headers
3.We can walk through the flow by clicking and observing the bottom of the canvas for the output and the flow
  our input is being truncated,filtered and compared for the analysis process
4.The output gives the repeat_donors_txt for repective years consequently listing everything rather than the latest years
5.Select the text format for the output with '|' and you can RUN the process
6.This can handle pretty large dataset and effective enough decisions can be made on each step along the walk through as 
  we can see how our data is getting modified.

