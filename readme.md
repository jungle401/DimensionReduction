
Eigenface Calculation using PCA:

Stack all normalized face images into a single matrix where each column represents a flattened face image. <br />
Compute the covariance matrix of the image matrix. <br />
Calculate the eigenvectors (principal components) and eigenvalues of the covariance matrix. These eigenvectors are referred to as "Eigenfaces." <br />
The Eigenfaces are ordered by their corresponding eigenvalues, and the top eigenfaces capture the most variance in the dataset. <br />

Eigenfaces:
<div>
    <img src="/output/eigenfaces/PCA/eigenface0.png" width=15% alt="Image 1">
    <img src="/output/eigenfaces/PCA/eigenface0.png" width=15% alt="Image 2">
    <img src="/output/eigenfaces/PCA/eigenface1.png" width=15% alt="Image 3">
    <img src="/output/eigenfaces/PCA/eigenface10.png" width=15% alt="Image 4">
    <img src="/output/eigenfaces/PCA/eigenface11.png" width=15% alt="Image 5">
    <img src="/output/eigenfaces/PCA/eigenface12.png" width=15% alt="Image 6">
    <img src="/output/eigenfaces/PCA/eigenface13.png" width=15% alt="Image 7">
    <img src="/output/eigenfaces/PCA/eigenface14.png" width=15% alt="Image 8">
    <img src="/output/eigenfaces/PCA/eigenface15.png" width=15% alt="Image 9">
    <img src="/output/eigenfaces/PCA/eigenface16.png" width=15% alt="Image 10">
    <img src="/output/eigenfaces/PCA/eigenface17.png" width=15% alt="Image 11">
    <img src="/output/eigenfaces/PCA/eigenface18.png" width=15% alt="Image 12">
    <img src="/output/eigenfaces/PCA/eigenface19.png" width=15% alt="Image 13">
    <img src="/output/eigenfaces/PCA/eigenface2.png" width=15%  alt="Image 14">
    <img src="/output/eigenfaces/PCA/eigenface20.png" width=15% alt="Image 15">
    <img src="/output/eigenfaces/PCA/eigenface21.png" width=15% alt="Image 16">
    <img src="/output/eigenfaces/PCA/eigenface22.png" width=15% alt="Image 17">
    <img src="/output/eigenfaces/PCA/eigenface23.png" width=15% alt="Image 18">
    <img src="/output/eigenfaces/PCA/eigenface3.png" width=15%  alt="Image 19">
    <img src="/output/eigenfaces/PCA/eigenface4.png" width=15%  alt="Image 20">
    <img src="/output/eigenfaces/PCA/eigenface5.png" width=15%  alt="Image 21">
    <img src="/output/eigenfaces/PCA/eigenface6.png" width=15%  alt="Image 22">
    <img src="/output/eigenfaces/PCA/eigenface7.png" width=15%  alt="Image 23">
    <img src="/output/eigenfaces/PCA/eigenface8.png" width=15%  alt="Image 24">
    <img src="/output/eigenfaces/PCA/eigenface9.png" width=15%  alt="Image 25">
</div>

Recognition:

To recognize a new face, project it into the Eigenspace formed by the Eigenfaces. <br />
Compare the coefficients obtained for the new face with the coefficients of known faces using a similarity measure (such as Euclidean distance or cosine similarity) to determine the closest match.<br />
