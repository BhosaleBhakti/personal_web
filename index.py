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
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css" integrity="sha512-5A8nwdMOWrSz20fDsjczgUidUBR8liPYU+WymTZP1lmY9G6Oc7HlZv156XqnsgNUzTyMefFTcsFH/tnJE/+xBg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
  <title>bhakti</title>
</head>

<body>
  <nav class="navbar navbar-expand-md  fixed-top maine-menu">
    <div class="container">
      <button class="navbar-toggler ml-auto" data-target="#my-nav" onclick="myFunction(this)" data-toggle="collapse"> <span class="bar1"></span> <span class="bar2"></span> <span class="bar3"></span> </button>
      <div id="my-nav" class="collapse navbar-collapse">
        <ul class="navbar-nav mx-auto">
          <li class="nav-item active"> <a class="nav-link" href="#">Home</a> </li>
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

  <div class="container-fluid fh5co-home-banner">
    <div class="card"> <img class="card-img" src="assets/img/m8.jpg" alt="" style="height:600px; width:100%;">
      <div class="card-img-overlay">
        <div class="center-text">
          <h2 class="card-title" style="font-family:algerian;">“Just one small positive thought in the morning can change your whole day.”</h2>
          <a href="#" class="btn">
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
 <div class="container-fluid fh5co-two-img">
    <div class="row">
      <div class="col-sm-6 pr-0 pl-0">
        <div class="card"> <img class="card-img" src="assets/img/m2.jpg" alt="" style="height:400px;>
          <div class="card-img-overlay"> </div>
        </div>
     
      <div class="col-sm-6 pr-0 pl-0">
        <div class="card"> <img class="card-img" src="assets/img/m16.jpg" alt="" style="height:400px;>
          <div class="card-img-overlay"> </div>
        </div>
      </div>
	   </div>
    </div>
  </div>

  <div class="container-fluid fh5co-recent-work" style="background-color:#fa86c4 !important;">
    <div class="container contact-pop">
      <div class="row">
        <div class="col-md-6  pr-0">
          <div class="card"> <img class="card-img w-100" src="assets/img/me1.jpg" alt="">
            <div class="card-img-overlay"> </div>
          </div>
        </div>
        <div class="col-md-6 pl-0" id="about">
          <div class="content">
            <h3 style="font-family:BELL MT">I am Bhakti Bhosale</h3>
            <h4 style="font-family:Arial Narrow; color:black; font-size:15px;"> Web Developer</h4>
            <hr />
            <p style="font-family:Arial Narrow;color:black;font-size:20px; font-family:Goudy Old Style;">Hi there! I’m Bhakti, a web developer with a strong passion for technology, design, and innovation. Currently, 
I am preparing for the MCA CET  to further academic journey and enhance my technical expertise.<br>  &nbsp;  &nbsp;  
&nbsp; "This website is a space to share my projects, ideas, & resources.
 Whether you're interested in Frontend Development, Backend Development 
 , you’ll find something valuable here."
</p>
            <a href="#" class="btn">CONTACT</a> </div>
			
			
          </div>
		  <div>

		  </div>
		   
	  
	  
	  
	  
	  
	  
	  
      <div class="container recent" id="activity">
        <div class="row">
          <h2 style="font-family:algerian; color:black;">Achievement</h2>
          <div class="owl-carousel owl-carousel2 owl-theme">
            <div>
              <div class="card"> <img class="card-img" src="assets/img/ac6.jpg" alt="">
                <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a>
                  <div class="bottom-text">
                    <h5 class="card-title" style="font-family:algerian;">PVK Nangnur[KS]</h5>
                    <p class="card-text">Teachers Day</p>
                  </div>
                </div>
              </div>
            </div>
            <div>
              <div class="card"> <img class="card-img" src="assets/img/ac7.jpg" alt="">
                <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a>
                  <div class="bottom-text">
                 <h5 class="card-title" style="font-family:algerian;">PVK Nangnur[KS]</h5>
                    <p class="card-text">Discus-Throw</p>
                  </div>
                </div>
              </div>
            </div>
            <div>
              <div class="card"> <img class="card-img" src="assets/img/ac8.jpg" alt="">
                <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a>
                  <div class="bottom-text">
                     <h5 class="card-title" style="font-family:algerian;">PVK Nangnur[KS]</h5>
                    <p class="card-text">Cricket</p>
                  </div>
                </div>
              </div>
            </div>
            <div>
              <div class="card"> <img class="card-img" src="assets/img/ac9.jpg" alt="">
                <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a>
                  <div class="bottom-text">
                    <h5 class="card-title" style="font-family:algerian;">PVK Nangnur[KS]</h5>
                    <p class="card-text">Ka</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="container-fluid recent fh5co-portfolio" id="portfolio">
    <div class="container">
    
      <h2 style="font-family:algerian; font-size:30px; color:black">MY Gallery</h2>
      <div class="row">
        <div class="bx bx-1">
        <div class="card"> <img class="card-img" src="assets/img/m2.jpg" alt="" style="width:300px; height:400px; ">
            <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a>
              <div class="bottom-text">
                <h5 class="card-title">Nature..</h5>
              </div>
            </div>
          </div>
        </div>
        <div class="bx bx-2">
           <div class="card"> <img class="card-img" src="assets/img/m3.jpg" alt="" style="width:300px; height:400px; ">
            <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a>
              <div class="bottom-text">
                <h5 class="card-title">farm..</h5>
              </div>
            </div>
          </div>
        </div>
        <div class="bx bx-3">
          <div class="card"> <img class="card-img" src="assets/img/m4.jpg" alt="" style="width:300px; height:400px; ">
            <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a>
              <div class="bottom-text">
                <h5 class="card-title">Tracking..</h5>
              </div>
            </div>
          </div>
        </div>
        <div class="bx bx-4">
          <div class="card"> <img class="card-img" src="assets/img/m5.jpg" alt="" style="width:300px; height:400px; ">
            <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a>
              <div class="bottom-text">
                <h5 class="card-title">Maharastrian Look..</h5>
              </div>
            </div>
          </div>
        </div>
        <div class="bx bx-middle" style="padding: 0;">
          <div class="bx bx-5">
             <div class="card"> <img class="card-img" src="assets/img/m6.jpg" alt="" style="width:300px; height:400px; ">
              <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a>
                <div class="bottom-text">
                  <h5 class="card-title">Sari..</h5>
                </div>
              </div>
            </div>
          </div>
          <div class="bx bx-6">
         <div class="card"> <img class="card-img" src="assets/img/m7.jpg" alt="" style="width:400px; height:300px; ">
              <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a>
                <div class="bottom-text">
                  <h5 class="card-title">Random..</h5>
                </div>
              </div>
            </div>
          </div>
          <div>
          
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="container-fluid fh5co-recent-work activity">
    <div class="container recent">
      <div class="row">
        <h2 style="font-family:algerian; color:black;">Projects..</h2>
        <div class="owl-carousel owl-carousel3 owl-theme">
          <div>
            <div class="card"> <img class="card-img" src="assets/img/shivraj.png" alt="" >
              <div class="card-img-overlay">
                <div class="bottom-text">
                  <h5 class="card-title">"Shivraj College Alumni"</h5>
                  <a href="project.py">Read more <img src="assets/img/double-right.svg" alt=""></a> 
                </div>
              </div>
            </div>
          </div>
          <div>
            <div class="card"> <img class="card-img" src="assets/img/sw.png"  alt="">
              <div class="card-img-overlay">
                <div class="bottom-text">
                  <h5 class="card-title">Swaraj Agrotech</h5>
                  <a href="project.py">Read more <img src="assets/img/double-right.svg" alt=""></a> 
                </div>
              </div>
            </div>
          </div>
          <div>
            <div class="card"> <img class="card-img" src="assets/img/wolfox.png" alt="">
              <div class="card-img-overlay">
                <div class="bottom-text">
                  <h5 class="card-title">IMS Laptop Store</h5>
                  <a href="project.py">Read more <img src="assets/img/double-right.svg" alt=""></a> 
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  
  

  
  
  
   <div class="container-fluid fh5co-about-me" id="testimonial" >
    <div id="my-carousel" class="carousel slide" data-ride="carousel" >
      <div class="carousel-inner">
        <div class="card"> <img class="card-img d-block w-100" src="assets/img/m8.jpg" alt="">
          <div class="card-img-overlay">
            <h2>Goals

 </h2>
          </div>
        </div>
		
	
        <div class="carousel-item">
          <div class="carousel-caption d-md-block"> <img src="assets/img/quote-icon.png" alt="">
            <p>To specialize in advanced web development techniques.
Good Communication Skills: I can collaborate effectively with team members and clients, ensuring clarity and understanding.<br>
To contribute meaningfully to the tech industry while continuing to grow professionally
<br>
Let’s connect and create something extraordinary together!</p>
          </div>
        </div>
        <div class="carousel-item active">
          <div class="carousel-caption d-md-block"> <img src="assets/img/quote-icon.png" alt="">
            <p>To specialize in advanced web development techniques.
Good Communication Skills: I can collaborate effectively with team members and clients, ensuring clarity and understanding.<br>
To contribute meaningfully to the tech industry while continuing to grow professionally
<br>
Let’s connect and create something extraordinary together!
.</p>
          </div>
        </div>
        <div class="carousel-item">
          <div class="carousel-caption d-md-block"> <img src="assets/img/quote-icon.png" alt="">
            <p>To specialize in advanced web development techniques.
Good Communication Skills: I can collaborate effectively with team members and clients, ensuring clarity and understanding.<br>
To contribute meaningfully to the tech industry while continuing to grow professionally
<br>
Let’s connect and create something extraordinary together!</p>
          </div>
        </div>
      </div>
	  <div >
      <ol class="carousel-indicators">
        <li data-target="#my-carousel" data-slide-to="0" > <img src="assets/img/m2.jpg" alt="" style=" border-radius:100%; height:80px;"> <span>Bhakti Bhosale</span> </li>
        <li class="active" data-target="#my-carousel" data-slide-to="1" aria-current="location"> <img src="assets/img/m3.jpg" alt="" style=" border-radius:100%; height:80px;"> <span>Bhakti Bhosale</span> </li>
        <li data-target="#my-carousel" data-slide-to="2"> <img src="assets/img/m8.jpg" alt="" style=" border-radius:100%; height:80px;"> <span>Bhakti Bhosale</span> </li>
      </ol></div>
    </div>
  </div>
  
  
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
  
  
  
  <-- test commit-->
  
  
  
  
  
  <footer class="container-fluid p-0 pr-0">
    <div class="row mr-0 ml-0" style="background-color:#fa86c4 !important;">
      <div class="col-md-6 pr-0 pl-0 map">
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d33667.6395514292!2d74.31593500896447!3d16.297656026572678!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc08cdfc33b51cf%3A0x895000d9edb09b36!2sBugatealur%2C%20Karnataka!5e1!3m2!1sen!2sin!4v1738282249565!5m2!1sen!2sin" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>      </div>
      <div class="col-md-6 content-us">
        <div class="contact-form" id="contact">
          <h3 class="text-uppercase">Contact me</h3>
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

</body>
</html>
''')