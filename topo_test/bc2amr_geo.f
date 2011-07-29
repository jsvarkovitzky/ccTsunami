
c
c ------------------------------------------------------------------
c
      subroutine bc2amr(val,aux,nrow,ncol,meqn,naux,
     1                  hx, hy, level, time, 
     2                  xleft,  xright,  ybot, ytop,
     3                  xlower, ylower,xupper,yupper,
     4                  xperiodic, yperiodic,spheredom)
 
c
c    Specific to geoclaw:  extrapolates aux(i,j,1) at boundaries
c    to constant.

c    Modified for wave-maker motion at bottom boundary.

c
c :::::::::: bc2amr ::::::::::::::::::::::::::::::::::::::::::::::;
c
c     Take a grid patch with mesh widths hx,hy, of dimensions nrow by
c     ncol,  and set the values of any piece of
c     of the patch which extends outside the physical domain 
c     using the boundary conditions. 
c
c     ------------------------------------------------
c     # Standard boundary condition choices for amr2ez in clawpack
c
c     # At each boundary  k = 1 (left),  2 (right),  3 (top), 4 (bottom):
c     #   mthbc(k) =  0  for user-supplied BC's (must be inserted!)
c     #            =  1  for zero-order extrapolation
c     #            =  2  for periodic boundary coniditions
c     #            =  3  for solid walls, assuming this can be implemented
c     #                  by reflecting the data about the boundary and then
c     #                  negating the 2'nd (for k=1,2) or 3'rd (for k=3,4)
c     #                  component of q.
c     #            =  4  sphere bcs (left half maps to right half of same 
c     #                  side, and vice versa), as if domain folded in half
c     ------------------------------------------------
c
c     The corners of the grid patch are at 
c        (xleft,ybot)  --  lower left corner
c        (xright,ytop) --  upper right corner
c
c     The physical domain itself is a rectangle bounded by
c        (xlower,ylower)  -- lower left corner
c        (xupper,yupper)  -- upper right corner
c     
c     the picture is the following: 
c
c               _____________________ (xupper,yupper)
c              |                     |  
c          _________ (xright,ytop)   |
c          |   |    |                |
c          |   |    |                |
c          |   |    |                |
c          |___|____|                |
c (xleft,ybot) |                     |
c              |                     |
c              |_____________________|
c   (xlower,ylower)
c        
c
c     Any cells that lie outside the physical domain are ghost cells whose
c     values should be set in this routine.  This is tested for by comparing
c     xleft with xlower to see if values need to be set at the left, as in
c     the figure above, and similarly at the other boundaries.
c
c     Patches are guaranteed to have at least 1 row of cells filled
c     with interior values so it is possible to  extrapolate. 
c     Fix trimbd if you want more than 1 row pre-set.
c
c     Make sure the order the boundaries are specified is correct
c     so that diagonal corner cells are also properly taken care of.
c
c     Periodic boundaries are set before calling this routine, so if the
c     domain is periodic in one direction only you
c     can safely extrapolate in the other direction. 
c
c     Don't overwrite ghost cells in periodic directions!

c     This particular routine bc2amr_noslopesets auxillary values so 
c     that no slope in topography occurs at the physical boundary.
c
c ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;

      implicit double precision (a-h,o-z)

      common /combc2/ mthbc(4)

      dimension val(nrow,ncol,meqn), aux(nrow,ncol,naux)
      logical xperiodic, yperiodic, spheredom

      hxmarg = hx*.01
      hymarg = hy*.01

      if (xperiodic .and. (yperiodic .or. spheredom)) go to 499
c
c
c-------------------------------------------------------
c     # left boundary:
c-------------------------------------------------------
      if (xleft .ge. xlower-hxmarg) then
c        # not a physical boundary -- no cells at this edge lies
c        # outside the physical bndry.
c        # values are set elsewhere in amr code.
         go to 199
         endif
c
c     # number of grid cells from this patch lying outside physical domain:
      nxl = (xlower+hxmarg-xleft)/hx
c
      go to (100,110,120,130) mthbc(1)+1
c
  100 continue
c     # wave-maker: wall moves with speed s
      smax = 0.00250d0
      beta = 1.0d0
      t0 = 0
      s = smax * 4/(dexp(-beta*(time - t0))+dexp(beta*(time - t0)))**2
c     s = smax*dexp(-beta*(time-t0)**2)

      if (dabs(s).lt.1.d-5) s = 0.d0
      do 105 m=1,meqn
         do 105 i=1,nxl
            do 105 j=1,ncol
                aux(i,j,1) =  aux(i,2*nyb+1-j,1) !inserted for bc2amr_noslope
                val(i,j,m) =  val(i,2*nyb+1-j,m)
  105       continue
c     # negate the normal velocity:
      do 106 j=1,nxl
         do 106 i=1,ncol
            val(i,j,3) = 2.d0 * s - val(i,j,3)
  106    continue
      go to 199

  110 continue
c     # zero-order extrapolation:
      do 115 m=1,meqn
         do 115 i=1,nxl
            do 115 j = 1,ncol
               aux(i,j,1) = aux(nxl+1,j,1)  !inserted for bc2amr_noslope
               val(i,j,m) = val(nxl+1,j,m)
  115       continue
      go to 199

  120 continue
c     # periodic:   handled elsewhere in amr
      go to 199

  130 continue
c     # solid wall (assumes 2'nd component is velocity or momentum in x):
      do 135 m=1,meqn
         do 135 i=1,nxl
            do 135 j = 1,ncol
               aux(i,j,1) = aux(2*nxl+1-i,j,1)  !inserted for bc2amr_noslope
               val(i,j,m) = val(2*nxl+1-i,j,m)
  135       continue
c     # negate the normal velocity:
      do 136 i=1,nxl
         do 136 j = 1,ncol
            val(i,j,2) = -val(i,j,2)
  136    continue
      go to 199

  199 continue
c
c-------------------------------------------------------
c     # right boundary:
c-------------------------------------------------------
      if (xright .le. xupper+hxmarg) then
c        # not a physical boundary --  no cells at this edge lies
c        # outside the physical bndry.
c        # values are set elsewhere in amr code.
         go to 299
         endif
c
c     # number of grid cells lying outside physical domain:
      nxr = (xright - xupper + hxmarg)/hx
      ibeg = max0(nrow-nxr+1, 1)
c
      go to (200,210,220,230) mthbc(2)+1
c
  200 continue
c     # user-specified boundary conditions go here in place of error output
      write(6,*) 
     &   '*** ERROR *** mthbc(2)=0 and no BCs specified in bc2amr'
      stop
      go to 299

  210 continue
c     # zero-order extrapolation:
      do 215 m=1,meqn
         do 215 i=ibeg,nrow
            do 215 j = 1,ncol
               aux(i,j,1) = aux(ibeg-1,j,1) !inserted for bc2amr_noslope
               val(i,j,m) = val(ibeg-1,j,m)
  215       continue
      go to 299

  220 continue
c     # periodic:   handled elsewhere in amr
      go to 299

  230 continue
c     # solid wall (assumes 2'nd component is velocity or momentum in x):
      do 235 m=1,meqn
         do 235 i=ibeg,nrow
            do 235 j = 1,ncol
               aux(i,j,1) = aux(2*ibeg-1-i,j,1) !inserted for bc2amr_noslope
               val(i,j,m) = val(2*ibeg-1-i,j,m)
  235       continue
c     # negate the normal velocity:
      do 236 i=ibeg,nrow
         do 236 j = 1,ncol
            val(i,j,2) = -val(i,j,2)
  236    continue
      go to 299

  299 continue
c
c-------------------------------------------------------
c     # bottom boundary:
c-------------------------------------------------------
      if (ybot .ge. ylower-hymarg) then
c        # not a physical boundary -- no cells at this edge lies
c        # outside the physical bndry.
c        # values are set elsewhere in amr code.
         go to 399
         endif
c
c     # number of grid cells lying outside physical domain:
      nyb = (ylower+hymarg-ybot)/hy
c
      go to (300,310,320,330) mthbc(3)+1
c
  300 continue
c     # wave-maker: wall moves with speed s
      smax = .00250d0
      beta = 1.0d0
      t0 = 0
      s = smax * 4/(dexp(-beta*(time - t0))+dexp(beta*(time - t0)))**2
c     s = smax*dexp(-beta*(time-t0)**2)

      if (dabs(s).lt.1.d-5) s = 0.d0
      do 305 m=1,meqn
         do 305 j=1,nyb
            do 305 i=1,nrow
                aux(i,j,1) =  aux(i,2*nyb+1-j,1) !inserted for bc2amr_noslope
                val(i,j,m) =  val(i,2*nyb+1-j,m)
  305       continue
c     # negate the normal velocity:
      do 306 j=1,nyb
         do 306 i=1,nrow
            val(i,j,3) = 2.d0 * s - val(i,j,3)
  306    continue
      go to 399
c
  310 continue
c     # zero-order extrapolation:
      do 315 m=1,meqn
         do 315 j=1,nyb
            do 315 i=1,nrow
                aux(i,j,1) = aux(i,nyb+1,1) !inserted for bc2amr_noslope
                val(i,j,m) = val(i,nyb+1,m)
  315       continue
      go to 399

  320 continue
c     # periodic:   handled elsewhere in amr
      go to 399

  330 continue
c     # solid wall (assumes 3'rd component is velocity or momentum in y):
      do 335 m=1,meqn
         do 335 j=1,nyb
            do 335 i=1,nrow
                aux(i,j,1) =  aux(i,2*nyb+1-j,1) !inserted for bc2amr_noslope
                val(i,j,m) =  val(i,2*nyb+1-j,m)
  335       continue
c     # negate the normal velocity:
      do 336 j=1,nyb
         do 336 i=1,nrow
            val(i,j,3) = -val(i,j,3)
  336    continue
      go to 399

  399 continue
c
c-------------------------------------------------------
c     # top boundary:
c-------------------------------------------------------
      if (ytop .le. yupper+hymarg) then
c        # not a physical boundary --  no cells at this edge lies
c        # outside the physical bndry.
c        # values are set elsewhere in amr code.
         go to 499
         endif
c
c     # number of grid cells lying outside physical domain:
      nyt = (ytop - yupper + hymarg)/hy
      jbeg = max0(ncol-nyt+1, 1)
c
      go to (400,410,420,430) mthbc(4)+1
c
  400 continue
c     # user-specified boundary conditions go here in place of error output
c     # wave-maker: wall moves with speed s
      smax = .083d0
      t0 = 2.0d0
#      s = -smax * 4/(dexp(-beta*(time - t0))-dexp(beta*(time - t0)))**2 #sech(x)^2
      if (dabs(s).lt.1.d-5) s = 0.d0
      do 405 m=1,meqn
         do 405 j=jbeg,ncol
            do 405 i=1,nrow
               aux(i,j,1) =  aux(i,2*jbeg-1-j,1)  !inserted for bc2amr_noslope
               val(i,j,m) =  val(i,2*jbeg-1-j,m)
  405       continue
c     # motion of the wall:
      do 406 j=jbeg,ncol
         do 406 i=1,nrow
            val(i,j,3) = 2.d0*s*val(i,j,1)-val(i,j,3)
  406    continue
      go to 499

  410 continue
c     # zero-order extrapolation:
      do 415 m=1,meqn
         do 415 j=jbeg,ncol
            do 415 i=1,nrow
               aux(i,j,1) = aux(i,jbeg-1,1)  !inserted for bc2amr_noslope
               val(i,j,m) =  val(i,jbeg-1,m)
  415       continue
      go to 499

  420 continue
c     # periodic:   handled elsewhere in amr
      go to 499

  430 continue
c     # solid wall (assumes 3'rd component is velocity or momentum in y):
      do 435 m=1,meqn
         do 435 j=jbeg,ncol
            do 435 i=1,nrow
               aux(i,j,1) =  aux(i,2*jbeg-1-j,1)  !inserted for bc2amr_noslope
               val(i,j,m) =  val(i,2*jbeg-1-j,m)
  435       continue
c     # negate the normal velocity:
      do 436 j=jbeg,ncol
         do 436 i=1,nrow
            val(i,j,3) = -val(i,j,3)
  436    continue
      go to 499

  499 continue

      return
      end

