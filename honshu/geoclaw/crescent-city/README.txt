begin_html  [use: doc/doc.css]
<!--   For a more readable version of this file, execute
                  unix>  make htmls
       in this directory and then point your browser to README.html 
     --------------------------------------------------------------  -->


<h2>
Honshu Event, 11 March 2011
</h2>
<h2>
Crescent City, California
</h2>

Some sample results are shown at
[http://www.clawpack.org/links/honshu2011].
The results posted 19 March 2011 were computed with this code as it appears
in Revision 65 of the svn repository:

[http://kingkong.amath.washington.edu/svn/tsunami-benchmarks/honshu/geoclaw/crescent-city]




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

The topography is in 
[link: ../../topo].  
(To retrieve you need to run [link: ../../topo/get_topo.py].)

The Subfault Format source parameters  are in
[link: ../../sources]
(To create dtopo files you need to run [link: ../../sources/make_topo.py].)

See [http://www.clawpack.org/users/topo.html]  for more information on
topography data formats.


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

