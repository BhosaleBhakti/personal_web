#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type:text/html\n")
print('''

<!DOCTYPE html>
<!--
  Girly by FreeHTML5.co
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
  <title>Bhakti</title>
  <style>
  .test{
  
   background-image: url(C:\wolfox\girly-master\girly-master\assets\img\back.jpg);
     background-color: #ff9999	;
  
  background-position: right bottom;
  background-repeat: no-repeat;
  padding: 100px 0;
  margin-top: 0; 
  
  
  }
  
  @import url("https://fonts.googleapis.com/css?family=Titillium+Web");
* {
  font-family: "Titillium Web", sans-serif;
}
body {
  height: 2000px;
}
.navbar .navbar-brand {
  font-size: 40px;
}
.navbar .nav-item {
  padding: 10px 20px;
}
.navbar .nav-link {
  font-size: 20px;
  margin-left: 10px;
}
.fa-bars {
  color: #007bff;
  font-size: 30px;
}


        img {
    max-width: 100%;
    height: auto;
}
        section {
            padding: 60px 0;
           /* min-height: 100vh;*/
        }
 ul {
            margin: 0;
            padding: 0;
            list-style: none;
        }
.contact-area {
    border-bottom: 1px solid #353C46;
	background-color:whitesmoke;
}

.contact-content p {
    font-size: 15px;
    margin: 30px 0 60px;
    position: relative;
}

.contact-content p::after {
    background: #353C46;
    bottom: -30px;
    content: "";
    height: 1px;
    left: 50%;
    position: absolute;
    transform: translate(-50%);
    width: 80%;
}

.contact-content h6 {
    color: #8b9199;
    font-size: 15px;
    font-weight: 400;
    margin-bottom: 10px;
}

.contact-content span {
    color: #353c47;
    margin: 0 10px;
}

.contact-social {
    margin-top: 30px;
}

.contact-social > ul {
    display: inline-flex;
}

.contact-social ul li a {
    border: 1px solid #8b9199;
    color: #8b9199;
    display: inline-block;
    height: 40px;
    margin: 0 10px;
    padding-top: 7px;
    transition: all 0.4s ease 0s;
    width: 40px;
}

.contact-social ul li a:hover {
    border: 1px solid #FAB702;
    color: #FAB702;
}

.contact-content img {
    max-width: 210px;
}

section, footer {
    background: #1A1E25;
    color: #868c96;
}

footer p {
    padding: 40px 0;
    text-align: center;
}

footer img {
    width: 44px;
}
body{
    margin-top:20px;
    background:#eee;
}
.gradient-brand-color {
    background-image: -webkit-linear-gradient(0deg, #376be6 0%, #6470ef 100%);
    background-image: -ms-linear-gradient(0deg, #376be6 0%, #6470ef 100%);
    color: #fff;
}
.contact-info__wrapper {
    overflow: hidden;
    border-radius: .625rem .625rem 0 0
}

@media (min-width: 1024px) {
    .contact-info__wrapper {
        border-radius: 0 .625rem .625rem 0;
        padding: 5rem !important
    }
}
.contact-info__list span.position-absolute {
    left: 0
}
.z-index-101 {
    z-index: 101;
}
.list-style--none {
    list-style: none;
}
.contact__wrapper {
    background-color: #fff;
    border-radius: 0 0 .625rem .625rem
}

@media (min-width: 1024px) {
    .contact__wrapper {
        border-radius: .625rem 0 .625rem .625rem
    }
}
@media (min-width: 1024px) {
    .contact-form__wrapper {
        padding: 5rem !important
    }
}
.shadow-lg {
    box-shadow: 0 1rem 3rem rgba(132,138,163,0.1) !important;
}

  </style>
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
           <li class="nav-item"> <a class="nav-link" href="project.py" tabindex="-1" aria-disabled="true">Projects</a></li> 
          <li class="nav-item"> <a class="nav-link" href="contact.py" tabindex="-1" aria-disabled="true">Contact</a></li>
        </ul>
      </div>
    </div>
  </nav>
  


  <div class="container-fluid fh5co-home-banner" >
    <div class="card"> <img class="card-img" src="assets/img/m8.jpg" alt="" style="height:600px; width:100%;">
      <div class="card-img-overlay">
        <div class="center-text">
          <h2 class="card-title" style="font-family:algerian;">"The best way to get a project done faster is to start sooner."</h2>
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
  
  
  
  
	
	
	
	
	<!-- <div class="container"><br><br> -->
    <!-- <div class="contact__wrapper shadow-lg mt-n9"> -->
        <!-- <div class="row no-gutters"> -->
            <!-- <div class="col-lg-5 contact-info__wrapper gradient-brand-color p-5 order-lg-2"> -->
                <!-- <h3 class="color--white mb-5">Contact</h3> -->
    
               
                <!-- <figure class="figure position-absolute m-0 opacity-06 z-index-100" style="bottom:0; right: 10px"> -->
                    <!-- <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="444px" height="626px"> -->
                        <!-- <defs> -->
                            <!-- <linearGradient id="PSgrad_1" x1="0%" x2="81.915%" y1="57.358%" y2="0%"> -->
                                <!-- <stop offset="0%" stop-color="rgb(255,255,255)" stop-opacity="1"></stop> -->
                                <!-- <stop offset="100%" stop-color="rgb(0,54,207)" stop-opacity="0"></stop> -->
                            <!-- </linearGradient> -->
    
                        <!-- </defs> -->
                        <!-- <path fill-rule="evenodd" opacity="0.302" fill="rgb(72, 155, 248)" d="M816.210,-41.714 L968.999,111.158 L-197.210,1277.998 L-349.998,1125.127 L816.210,-41.714 Z"></path> -->
                        <!-- <path fill="url(#PSgrad_1)" d="M816.210,-41.714 L968.999,111.158 L-197.210,1277.998 L-349.998,1125.127 L816.210,-41.714 Z"></path> -->
                    <!-- </svg> -->
                <!-- </figure> -->
            <!-- </div> -->
 
            <!-- <!-- End Contact Form Wrapper --> 
    
        <!-- </div> -->
 <!--    </div> -->
<!-- </div> -->


          

		
    </section>
		  
        </div>
      </div>
	 
	  
	  
	  

  
  <div class="col-md-12" style="background-color:#fa86c4 !important;  ">
    <div class="container-fluid fh5co-home-banner" >
    <div class="card"> <img class="card-img" src="assets/img/m25.jpg" alt="" style="height:900px; ">
      <div class="card-img-overlay">
        <!-- <div class="center-text"> -->
   <div class="row">
  	<div class="col-lg-12" >
	<div class="row">
	<div class="col-lg-4"></div>
		<div class="col-lg-4">
	<!-- <h1 style="text-align:center; font-family:Berlin Sans FB Demi; font-size:60px;"><span style="color:blue;">Contact</span></h1> -->
		<div class="col-md-12" style="height:50px;"></div>
	<ul>
	<h1 style="text-align:center; font-size:30px;color:blue;"><i class="fa fa-address-book" aria-hidden="true"></i> &nbsp Address</h1>
	<br><h1 style="font-family:Constantia; font-size:30px; color:white;"> Karnatka , Tal-Hukkeri , Dist-Belgaum , Village-Bugate Alur , Pin code- 591313 </h1></div>
	<div class="col-lg-4"></div>
	</div>
	</div>
	
	<div class="col-md-12" style="height:50px;"></div>
  
  	<div class="col-lg-12" >
	<div class="row">
	<div class="col-lg-4"></div>
		<div class="col-lg-4">
	<ul>
	<h1 style="text-align:center; font-size:30px;color:blue;"> <i class="fa fa-phone" ></i> &nbsp Phone no</h1><br>
	<h1 style="text-align:center; font-family:Constantia; font-size:30px; color:white; ">+91 9019696460<br>+91 9019251822</h1></div>
	<div class="col-lg-4">
	</div>
	</div>
	</div>
		<div class="col-md-12" style="height:50px;"></div>

  
  	<div class="col-lg-12" >
	<div class="row">
	<div class="col-lg-4"></div>
		<div class="col-lg-4">
	<ul>
	<h1 style="text-align:center; font-size:30px;color:blue;"> <i class="fa fa-envelope" ></i> &nbsp; Email</h1>
	<br><h1 style="text-align:center font-family:Constantia; font-size:29px; color:white;">bhosalebhakti2003@gamil.com<br>bhosaleb363@gmail.com</h1></div>
	<div class="col-lg-4">
	</div>
	</div>
	</div>
	</div><br><br>
	</div>
    </div>
  </div></div>
  <!-- </div> -->
  <!-- <div style="width:50%;margin: 40px auto;background:#eee;border: 2px solid black; "> -->
  <!-- <h1 style="color:black; font-family:algerian; margin-left:40%;"> ME</h1> -->
  <!-- <div id="carouselExampleControls" class="carousel slide" data-ride="carousel"> -->
  <!-- <div class="carousel-inner"> -->
    <!-- <div class="carousel-item active"> -->
      <!-- <img class="d-block w-100" src="assets/img/f16.jpg" alt="First slide" style="height:380px;"> -->
    <!-- </div> -->
    <!-- <div class="carousel-item"> -->
      <!-- <img class="d-block w-100" src="assets/img/f18.jpg" alt="Second slide" style="height:380px;"> -->
    <!-- </div> -->
    <!-- <div class="carousel-item"> -->
      <!-- <img class="d-block w-100" src="assets/img/f22.jpg" alt="Third slide" style="height:380px;"> -->
    <!-- </div> -->
	 <!-- <div class="carousel-item"> -->
      <!-- <img class="d-block w-100" src="assets/img/f24.jpg" alt="Third slide" style="height:380px;"> -->
    <!-- </div> -->
	 <!-- <div class="carousel-item"> -->
      <!-- <img class="d-block w-100" src="assets/img/f20.jpg" alt="Third slide" style="height:380px;"> -->
    <!-- </div> -->
	 <!-- <div class="carousel-item"> -->
      <!-- <img class="d-block w-100" src="assets/img/f12.jpg" alt="Third slide" style="height:380px;"> -->
    <!-- </div> -->
  <!-- </div> -->
  <!-- <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev"> -->
    <!-- <span class="carousel-control-prev-icon" aria-hidden="true"></span> -->
    <!-- <span class="sr-only">Previous</span> -->
  <!-- </a> -->
  <!-- <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next"> -->
    <!-- <span class="carousel-control-next-icon" aria-hidden="true"></span> -->
    <!-- <span class="sr-only">Next</span> -->
  <!-- </a> -->
<!-- </div> -->
<!-- </div> -->
  
  
  
  


  
  
  
  <div class="container-fluid fh5co-insta-feed activity">
    <div class="container recent">
      <div class="row mb-5 pb-5">
        <div class="col-lg-6">
          <div class="twit-box">
            <div class="media mb-3"> <img class="align-self-start mr-3 rounded-circle" src="assets/img/m2.jpg" alt="" style="height:70px; width:70xpx;">
              <div class="media-body">
                <h5 class="mb-0 mt-3">Bhakti Bhosale</h5>
                <p>bhosalebhakti2003@gmail.com</p>
              </div>
            </div>
            <p class="text-justify"  style="font-family:Goudy Old Style;">Hi there! I’m Bhakti, a web developer with a strong passion for technology, design, and innovation. Currently, 
I am preparing for the MCA CET 2015 to further advance my academic journey and enhance my technical expertise.<br>  &nbsp;  &nbsp;  
&nbsp; "This website is a space to share my projects, ideas, and resources.
 Whether you're interested in Frontend Development , Backend Development 
 , you’ll find something valuable here."  </p>
            <div class="clearfix"> <a href="#" class="btn btn-primary mt-2 float-right">Follow</a> </div>
          </div>
        </div>
        <div class="col-lg-6 feed-caro">
           <h2 style="font-family:Goudy Stout; color:black;">Skills..</h2>
          <div class="owl-carousel owl-carousel4 owl-theme">
            <div>
              <div class="card"> <img class="card-img" src="assets/img/skill.png" alt="">
                <div class="card-img-overlay"> </div>
              </div>
            </div>
            <div>
              <div class="card"> <img class="card-img" src="assets/img/skill1.jpg"  alt="" style="height:310px;">
                <div class="card-img-overlay"> </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <h2 class="text-center d-block">Find me on social media</h2>
      <div class="row social-links">
        <ul class="nav mx-auto">
          
           <li class="nav-item"> <a class="nav-link" href="https://t.me/Anonymous_14_9"><img src="assets/img/teli1.png " style="height:50px; width:50px; border-radius:80px;margin-top:-12px; margin-left:-1px;" alt=""></a> </li>
          <li class="nav-item"> <a class="nav-link" href="https://whatsapp.com/dl/ "><img src="assets/img/wp.png" style="height:50px; width:50px; border-radius:80px;margin-top:-12px; margin-left:-1px; border:1px solid black;"alt=""></a> </li>
          <li class="nav-item"> <a class="nav-link" href="https://www.linkedin.com/in/bhakti-bhosale-228a25284?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"><img src="assets/img/li.png" style="height:50px; width:50px; border-radius:80px;margin-top:-12px; margin-left:-1px; border:1px solid black;" alt=""></a> </li>
          <li class="nav-item"> <a class="nav-link" href="https://www.instagram.com/bhaktii_bhosale?igsh=N3AwN2R1M3Zwd2l2"><img src="assets/img/in2.png" style="height:50px; width:50px; border-radius:80px;margin-top:-12px; margin-left:-1px; border:1px solid black;" alt=""></a> </li>
        </ul>
      </div>
    </div>
  </div>
  
    <footer class="container-fluid p-0 pr-0" style="background-color:whitesmoke !important;">
    <div class="row mr-0 ml-0"  style="background-color:pink !important;">
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
	<div class="copy pt-4 pb-4" >
      <p><a href="https://freehtml5.co/" target="_blank"> &copy; 2025</a>  &nbsp;  |  &nbsp; Design by <a href="https://freehtml5.co/" target="_blank">Bhakti Bhosale</a> &nbsp; &nbsp;  </p>
    </div>
   
  </footer>
  
  
  
  
  
  
  


  <!-- jQuery first, then Popper.js, then Bootstrap JS --> 
  <script src="assets/js/jquery-3.3.1.slim.min.js"></script> 
  <script src="assets/js/popper.min.js" ></script> 
  <script src="assets/js/bootstrap.min.js"></script> 
  <script src="assets/js/owl.carousel.min.js"></script> 
  <script src="assets/js/main.js"></script>
  
  <script>$('#carouselExampleControls').carousel();</script>

</body>
</html>
''')