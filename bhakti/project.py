#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type:text/html\n")
print('''
<!DOCTYPE html>
<!--
  Girly by FreeHTML5.cos
  Twitter: https://twitter.com/fh5co
  Facebook: https://fb.com/fh5co
  URL: https://freehtml5.co
-->
<html lang="en">
<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="stylesheet" href="assets/css/bootstrap.min.css">
  <link rel="stylesheet" href="assets/css/style.css">
  <title>Girly</title>
</head>

<body>
   <nav class="navbar navbar-expand-md  fixed-top maine-menu">
    <div class="container">
      <button class="navbar-toggler ml-auto" data-target="#my-nav" onclick="myFunction(this)" data-toggle="collapse"> <span class="bar1"></span> <span class="bar2"></span> <span class="bar3"></span> </button>
      <div id="my-nav" class="collapse navbar-collapse">
        <ul class="navbar-nav mx-auto">
          <li class="nav-item active"> <a class="nav-link" href="index.py">Home</a> </li>
          <li class="nav-item"> <a class="nav-link" href="about.py" tabindex="-1" aria-disabled="true">About</a></li>
          <li class="nav-item"> <a class="nav-link" href="gallery.py" tabindex="-1" aria-disabled="true">Gallery</a></li>
          <li class="nav-item"> <a class="nav-link" href="achievement.py" tabindex="-1" aria-disabled="true">Achievement</a></li>
          <!-- <li class="nav-item"> <a class="nav-link" href="#testimonial" tabindex="-1" aria-disabled="true">Testimonial</a></li> -->
           <li class="nav-item"> <a class="nav-link" href="project.py" tabindex="-1" aria-disabled="true">Project</a></li> 
          <li class="nav-item"> <a class="nav-link" href="contact.py" tabindex="-1" aria-disabled="true">Contact</a></li>
        </ul>
      </div>
    </div>
  </nav>

  <div class="container-fluid fh5co-home-banner" >
    <div class="card"> <img class="card-img" src="assets/img/m8.jpg" alt="" style="height:600px; ">
      <div class="card-img-overlay">
        <div class="center-text">
          <h2 class="card-title">"Code is like humor. When you have to explain it, it’s bad."</h2>
          <a href="index.py" class="btn">
            <svg width="201" height="51" viewBox="0 0 201 51">
              <defs>
                <style>
                .cls-1 {
                  fill: none;
                  stroke-width: 1px;
                  stroke: url(#linear-gradient);
                }
              </style>
              <linearGradient id="linear-gradient" x1="140.508" y1="50.5" x2="60.492" y2="0.5" gradientUnits="userSpaceOnUse">
                <stop offset="0" stop-color="#e90e65"/>
                <stop offset="1" stop-color="#fff"/>
              </linearGradient>
            </defs>
            <rect id="Rounded_Rectangle_1" data-name="Rounded Rectangle 1" class="cls-1" x="0.5" y="0.5" width="200" height="50" rx="25" ry="25"/>
          </svg>
        Explore</a> </div>
      </div>
    </div>
  </div>


  <!-- Blog content section -->
  <section class="fh5co-blog-content" style="background-color:#fa86c4 !important;">

    <div class="blog-content-bckg">
      <div class="blog-content-inner" style="background-color:#fa86c4 !important;">
        <div class="container-fluid">
          <h2 class="card-title" style=" font-family:Broadway; color:brown;">My projects..</h2>
          <div class="row single-blog">
            <div class="col-xl-4 col-lg-12 single-blog__img">
              <img class="card-img w-100" src="assets/img/shivraj.png" alt="" style="height:250px;" >
            </div>
            <div class="col-xl-8 col-lg-12 single-blog__text">
              <h2 style="font-size:25px; font-family:Bernard MT Condensed; color:black;"> Shivraj Collage Alumni</h2><hr class="my-4">
              <p style="font-size:20px; font-family:Bell MT; color:black;">
 &nbsp;  &nbsp;  &nbsp; "Shivraj College Alumni" is a web-based platform designed to connect alumni of Shivraj College. It was built using HTML, CSS, Java, and MySQL for database management. The project allows alumni to register,
communicate, and share updates about their professional journeys. It enhances networking opportunities and maintains a strong alumni connection... </p>
              <p style="font-size:20px; font-family:Bell MT;color:black;">  &nbsp;  &nbsp;  &nbsp; The greatest asset any institution can have is the Alumni system. Alumni are the people who represent the institution in the real world.
			  Alumni website is created for the students that have graduated from the institution. This is an online website that allows former students to take advantage of the benefits and services that an institution offers after graduation. 
			  The alumni network is becoming important in the development of the institution because of their vast potential that benefits both the institution and the students..</p>
            </div>
			    <p>
          <a class="btn btn-secondary" href="http://localhost:23879/collage_alumni/" target="_blank" role="button" style="margin-left:350%;">
           <span style="font-size:15px;"> View Project<span><i class="fa fa-chevron-right" aria-hidden="true"></i>
          </a>
        </p>
          </div>
          <div class="row single-blog">
            <div class="col-xl-4 col-lg-12 single-blog__img">
              <img class="card-img w-100" src="assets/img/sw.png" alt="" style="height:250px;">
            </div>
            <div class="col-xl-8 col-lg-12 single-blog__text">
  <h2 style="font-size:25px; font-family:Bernard MT Condensed; color:black;">Swaraj Agrotech</h2> <hr class="my-4">
              <p style="font-size:20px; font-family:Bell MT; color:black;">  &nbsp;  &nbsp;  &nbsp; "Swaraj Agrotech" is a web-based platform designed to support agricultural businesses by providing an online marketplace for farmers and customers. It is developed using HTML, CSS, Bootstrap, PHP, and MySQL, ensuring a dynamic and interactive user experience.
        The homepage features an overview of the platform, showcasing various agricultural products such as seeds, fertilizers, and farming tools. A navigation bar allows users to browse different categories, making it easy to find specific products.
        The product catalog displays a wide range of agricultural items with images, descriptions, and prices.</p>

		<p style="font-size:20px; font-family:Bell MT; color:black;"> &nbsp;  &nbsp;  &nbsp; Users can utilize the search and filter functionality to sort products based on type, price, and availability.
        A product details page provides in-depth information about each item, including benefits, usage instructions, and customer reviews. The shopping cart functionality enables users to add products and proceed to checkout.   </p>
            </div>
			    <p>
          <a class="btn btn-secondary" href="file:///C:/wolfox/Swaraj.html" target="_blank" role="button" style="margin-left:350%;">
           <span style="font-size:15px;"> View Project<span><i class="fa fa-chevron-right" aria-hidden="true"></i>
          </a>
        </p>
          </div>
          <div class="row single-blog">
            <div class="col-xl-4 col-lg-12 single-blog__img">
              <img class="card-img w-100" src="assets/img/ims.png" alt="" style="height:250px;">
            </div>
            <div class="col-xl-8 col-lg-12 single-blog__text">
                      <h2 style="font-size:25px; font-family:Bernard MT Condensed; color:black;" >IMS Laptop Store</h2><hr class="my-4">
               <p style="font-size:20px; font-family:Bell MT; color:black;"> &nbsp;  &nbsp;  &nbsp; "IMS Laptop Store" is an e-commerce website designed for selling laptops online. It is developed using HTML, CSS, and Bootstrap, ensuring a responsive and visually appealing user interface.
        The website features a homepage showcasing the latest laptop models with images, specifications, and prices. A navigation bar allows users to browse different categories, such as gaming laptops, business laptops, and budget-friendly options.
       The product catalog page displays laptops with detailed descriptions, making it easy for users to compare models.  <p>

		<p style="font-size:20px; font-family:Bell MT; color:black;"> &nbsp;  &nbsp;  &nbsp; A search and filter functionality helps users find laptops based on brand, price, and specifications.
        The product details page provides in-depth information about each laptop, including technical specifications, reviews, and customer ratings. The cart system allows users to add items for purchase and proceed to checkout seamlessly.
        Using Bootstrap, the website is fully responsive, making it accessible on desktops, tablets, and mobile devices. The modern UI design enhances the user experience, ensuring easy navigation and smooth interactions.
        Overall, "IMS Laptop Store" is an efficient and user-friendly e-commerce solution, offering a seamless shopping experience for laptop buyers.</p> 
            </div>
			    <p>
          <a class="btn btn-secondary" href="file:///C:/wolfox/index.html" target="_blank" role="button" style="margin-left:350%;">
           <span style="font-size:15px;"> View Project <span><i class="fa fa-chevron-right" aria-hidden="true"></i>
          </a>
        </p>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- Blog content section end -->


  <footer class="container-fluid p-0 pr-0" style="background-color:pink !important;" >
    <div class="row mr-0 ml-0">
      <div class="col-md-6 pr-0 pl-0 map">
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d33667.6395514292!2d74.31593500896447!3d16.297656026572678!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc08cdfc33b51cf%3A0x895000d9edb09b36!2sBugatealur%2C%20Karnataka!5e1!3m2!1sen!2sin!4v1738318596690!5m2!1sen!2sin" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>      </div>
      <div class="col-md-6 content-us">
        <div class="contact-form">
          <h3 class="text-uppercase">Contact with me</h3>
          <input type="text" class="form-control" placeholder="Your Name">
          <input type="text" class="form-control" placeholder="Your Email">
          <textarea class="form-control" placeholder="Your Message"></textarea>
          <button type="submit">Send</button>
        </div>
      </div>
    </div>
    <div class="copy pt-4 pb-4">
      <p><a href="https://freehtml5.co/" target="_blank"> &copy; 2025</a>  &nbsp;  |  &nbsp; Design by <a href="https://freehtml5.co/" target="_blank">Bhakti Bhosale</a> &nbsp; &nbsp;  </p>
    </div>
  </footer>

  <!-- jQuery first, then Popper.js, then Bootstrap JS --> 
  <script src="assets/js/jquery-3.3.1.slim.min.js"></script> 
  <script src="assets/js/popper.min.js" ></script> 
  <script src="assets/js/bootstrap.min.js"></script> 
  <script src="assets/js/owl.carousel.min.js"></script> 
  <script src="assets/js/main.js"></script>

</body>
</html>
''')