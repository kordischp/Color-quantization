<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  
<h3 align="center">Image color quantization</h3>

  <p align="center">
    A simple program for image color quantization using 2 methods with an option to resize images.
</div>


<!-- ABOUT THE PROJECT -->
## About The Project


Performs a pixel-wise Vector Quantization (VQ) of an image, reducing the number 
of colors required to show the image, then saves the images created using 
K-means and random methods. K-means finds average colors to use for modified 
image, random method selects them at random from the original image. Random 
method sometimes can give better results at low color number. The program has an
option to resize an image before performing color quantization - useful for 
creating nonograms.


<!-- USAGE EXAMPLES -->
## Usage

To use the program, specify the parameters inside the code. By default the program takes
an image named 'image.jpg' and reduces the number of colors to 10. Parameters 'pixelize' 
and 'fsize' are only needed if image needs to be resized. If no image is found then a sample
is loaded.

![alt text](/images/image1.png)


Running the program on a sample image gives the following results for 10 colors:

![alt text](/images/image2.png)

The 2 images are then saved separately in the working folder.


<!-- GETTING STARTED -->
## Prerequisites

To run the program, a few packages are required:

* numpy
  ```sh
  pip install numpy
  ```
* matplotlib
  ```sh
  pip install matplotlib
  ```
* scikit-learn
  ```sh
  pip install scikit-learn
  ```
* Pillow (PIL)
  ```sh
  pip install Pillow
  ```
* scikit-image
  ```sh
  pip install scikit-imag
  ```


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

This code is a modification of the following code:

* Authors: Robert Layton <robertlayton@gmail.com>,
         Olivier Grisel <olivier.grisel@ensta.org>,
         Mathieu Blondel <mathieu@mblondel.org>.
* License: BSD 3 clause
* Source:  https://scikit-learn.org/stable/auto_examples/cluster/plot_color_quantization.html

