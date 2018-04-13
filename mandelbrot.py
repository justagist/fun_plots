import sys
import numpy as np
import matplotlib.pyplot as plt



class MandelbrotSet:

    '''
        Mandelbrot set is the set of complex numbers c for which the function f(z) = z*z + c, does not diverge when iterated from z = 0, z = f(z=0), z = (f(f(z=0)))...

        Plotting the mandelbrot set (the Mandelbrot Atlas) will produce a beautiful fractal pattern.

            The plot:
                - Real values on one axis and imaginary values on the other.
                - The colour of each point on the plot depends on the number of iterations required for the mandelbrot function to diverge for the corresponding complex number.

    '''

    def __init__(self, xlim = [-0.22, -0.219], ylim = [-0.70, -0.699], density = 1000, iteration_threshold = 120):

        '''
            xlim, ylim: The limits of the Atlas plot
            density: The number of points along each axis
            iteration_threshold: The number of iterations before the function is declared undiverging for the complex number

        '''

        self._set_axes(xlim, ylim, density)

        self._initialise_atlas()
        self._find_mandelbrot_set(iteration_threshold)

        self._visualise_atlas()


    def _set_axes(self, xlim, ylim, density):

        '''
            Setting the axes for the Mandelbrot Atlas
        '''

        self.real_axis_ = np.linspace(xlim[0], xlim[1], density)
        self.imaginary_axis_ = np.linspace(ylim[0], ylim[1], density)

        self.len_r_axis_ = len(self.real_axis_)
        self.len_i_axis_ = len(self.imaginary_axis_)


    def _initialise_atlas(self):
        '''
            Creating the empty atlas of required size
        '''

        self.atlas_ = np.empty((self.len_r_axis_, self.len_i_axis_))


    def _find_mandelbrot_set(self, threshold):
        '''
            Find the number of iterations required for the function to diverge for each real-imaginary pair in the atlas and populate the atlas with the corresponding iteration value.
        '''

        def count_num_iterations_to_divergence(complex_num, threshold):

            z = complex(0, 0)

            for iteration in xrange(threshold):
                z = mandelbrot_val(z, complex_num)

                if abs(z) > 4:
                    break
                    pass
                pass
            return iteration + 1

        def mandelbrot_val(z, comp_num):
            '''
                The Mandelbrot function
            '''
            return (z*z) + comp_num


        for ix in xrange(self.len_r_axis_):
            for iy in xrange(self.len_i_axis_):
                cx = self.real_axis_[ix]
                cy = self.imaginary_axis_[iy]
                c = complex(cx, cy)

                self.atlas_[ix, iy] = count_num_iterations_to_divergence(c, threshold)
                pass
            pass

    def _visualise_atlas(self):
        '''
            Visualise the populated atlas
        '''
        plt.figure("Mandelbrot Atlas")
        plt.imshow(self.atlas_.T, interpolation="nearest")
        plt.show()


if __name__ == '__main__':

    if len(sys.argv) > 1 and sys.argv[1] == '2':
        xl = [-0.22, -0.219]
        yl = [-0.70, -0.699]
    else:
        xl = [-2.25, 0.75]
        yl = [-1.5, 1.5]

    MandelbrotSet(xlim = xl, ylim = yl)
    # MandelbrotSet()
