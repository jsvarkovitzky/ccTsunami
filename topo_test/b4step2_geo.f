c     ============================================
      subroutine b4step2(maxmx,maxmy,mbc,mx,my,meqn,q,
     &            xlower,ylower,dx,dy,t,dt,maux,aux)
c     ============================================
c
c     # called before each call to step
c     # use to set time-dependent aux arrays or perform other tasks.
c
c     This particular routine sets negative values of q(i,j,1) to zero,
c     as well as the corresponding q(i,j,m) for m=1,meqn.
c     This is for problems where q(i,j,1) is a depth.
c     This should occur only because of rounding error.

c     Also calls movetopo if topography might be moving.

      use geoclaw_module
      use topo_module
      use dtopo_module


      implicit double precision (a-h,o-z)

      parameter (maxm=500)
      common /comhmax/ hmax(maxm,maxm)

      dimension q(1-mbc:maxmx+mbc,1-mbc:maxmy+mbc, meqn)
      dimension aux(1-mbc:maxmx+mbc,1-mbc:maxmy+mbc, maux)


c=====================Parameters===========================================

      if ((mx.gt.maxm) .or. (my.gt.maxm)) then
         write(6,*) '*** Need to increase maxm in b4step2'
         stop
         endif

c     # check for NANs in solution:
      call check4nans(maxmx,maxmy,meqn,mbc,mx,my,q,t,1)

c     # check for h < 0 and reset to zero
c     # check for h < drytolerance
c     # set hu = hv = 0 in all these cells

      do i=1-mbc,mx+mbc
        do j=1-mbc,my+mbc
          if (q(i,j,1).lt.drytolerance) then
             q(i,j,1) = max(q(i,j,1),0.d0)
             do m=2,meqn
                q(i,j,m)=0.d0
                enddo
             endif
        enddo
      enddo

      write(26,*) 'B4STEP2: t, num_dtopo: ', t,num_dtopo
      do i=1,num_dtopo
          call movetopo(maxmx,maxmy,mbc,mx,my,
     &      xlower,ylower,dx,dy,t,dt,maux,aux,
     &      dtopowork(i0dtopo(i):i0dtopo(i)+mdtopo(i)-1),
     &      xlowdtopo(i),ylowdtopo(i),xhidtopo(i),yhidtopo(i),
     &      t0dtopo(i),tfdtopo(i),dxdtopo(i),dydtopo(i),dtdtopo(i),
     &      mxdtopo(i),mydtopo(i),mtdtopo(i),mdtopo(i),
     &      minleveldtopo(i),maxleveldtopo(i),topoaltered(i))
      enddo

      if (t .eq. 0.d0) then
          write(6,*) 'initializing hmax...'
          do i=1,mx
             do j=1,my
                hmax(i,j) = 0.d0
                enddo
              enddo
          endif

      do i=1,mx
         do j=1,my
            hmax(i,j) = dmax1(hmax(i,j), q(i,j,1))
            enddo
          enddo

      return
      end
