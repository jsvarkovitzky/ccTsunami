begin_html  [use: doc/doc.css]
<!--   For a more readable version of this file, execute
                  unix>  make htmls
       in this directory and then point your browser to README.html 
     --------------------------------------------------------------  -->


<h2>
Honshu Event, 11 March 2011
</h2>
<h2>
Multiple DART Buoy Comparison
</h2>

Some sample results are shown at
[http://www.clawpack.org/links/honshu2011].
The results posted 15 March 2011 were computed with this code as it appears
in Revision ?? of the svn repository:

[http://kingkong.amath.washington.edu/svn/tsunami-benchmarks/honshu/geoclaw/multidart]

The DART data was detided using scripts in

[http://kingkong.amath.washington.edu/svn/tsunami-benchmarks/honshu/DART].

See [code: maketopo.py].  This downloads topography data from the 
[http://kingkong.amath.washington.edu/topo/ GeoClaw topography database]
that originally came from the
NOAA National Geophysical Data Center (NGDC)
using [http://www.ngdc.noaa.gov/mgg/gdas/gd_designagrid.html Design-a-grid].

See [http://www.clawpack.org/users/topo.html]  for more information on
topography data formats.

The Subfault Format source parameters are in 
[link: honshu-ucsb3.txt].
This was downloaded from the following sites on 14 March 2011.


UCSB site for earthquake data:
[http://www.geol.ucsb.edu/faculty/ji/big_earthquakes/2011/03/0311/Honshu_main.html]


See instructions on bottom of page.

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


<dt>[code: setprob.f]
<dd>
Standard for for GeoClaw


</dl>

<h4>
Python files
</h4>
<dl>

<dt>[code: maketopo.py]
<dd> Used to create topo file and dtopo data file.

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

You must first download and install Clawpack.  Version 4.6 was used for
these tests.  See
[http://www.clawpack.org/users] for instructions and downloads.

You need to make sure your Unix environment variables are set properly as
described in the the documentation.  For this example you also need to insure
that PYTHONPATH includes the directory tsunami-benchmarks/datatools.

To make topo and dtopo data files:
{{{
  $ make topo
}}}

This downloads some topo files and creates the dtopo files honshu-usgs.tt1
and honshu-ucsb.tt1 by applying the Okada model to the corresponding .txt
files.

Select the source to be used to either honshu-usgs.tt1 or honshu-ucsb.tt1 in
[code: setrun.py].

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

All of this can be done with:

{{{
  $ source make_all.sh
}}}

For more documentation, see [http://www.clawpack.org/users].

end_html

