begin_html  [use: doc/doc.css]
<!--   For a more readable version of this file, execute
                  unix>  make htmls
       in this directory and then point your browser to README.html 
     --------------------------------------------------------------  -->

<h2>
Conical Island Wave Tank Benchmark
</h2>
This is a test of the wave tank experiment summarized at the

<b>benchmark site</b>:
[http://nctr.pmel.noaa.gov/benchmark/Laboratory/Laboratory_ConicalIsland/index.html]



This is a first pass at setting up this problem, but the gauges are not in
correct positions and the boundary conditions probably aren't correct.




<h4>
Plots of results
</h4>
After running this code and creating plots via "make .plots", you should be
able to view the plots in [link: _plots/_PlotIndex.html].


<h4>
Fortran files
</h4>


<dl>
<dt>[code: Makefile]
<dd> Determines which version of fortran files
are used when compiling the code with make and specifies where output and
plots should be directed.  Type "make .help" at the Unix prompt for options.


<dt>[code: bc2amr_geo.f]
<dd>
Sets boundary conditions each time step.  Boundary conditions at the bottom
boundary y = ylower are specified to simulate motion of a wave paddle.


</dl>

<h4>
Python files
</h4>
<dl>

<dt>[code: maketopo.py]
<dd> Used to create topo file.

<dt>[code: setrun.py]
<dd> This file contains a function that 
specifies what run-time parameters will be used.

<dt>[code: setplot.py]
<dd> This file contains a function that 
specifies what plots will be done and
sets various plotting parameters. 

</dl>


<h4>
Data files
</h4>

The .data files are automatically generated using the information in 
[code: setrun.py].


<h4>
Instructions
</h4>


To make topo and qinit data files:
{{{
  $ python maketopo.py
}}}

To make all data files, edit setrun.py and then
{{{
  $ make .data
}}}

To run code:
{{{
  $ make .output
}}}

To plot results, either generate html pages via:
{{{
  $ make .plots
}}}
or view interactively using ipython and Iplotclaw.

end_html

