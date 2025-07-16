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
  .a{
  margin-top:10px !important;
  }
  .test{
  
   background-image: url(C:\wolfox\girly-master\girly-master\assets\img\back.jpg);
     background-color: #ff9999	;
  
  background-position: right bottom;
  background-repeat: no-repeat;
  padding: 100px 0;
  margin-top: 0; 
  
  
  }
  .ct-socials {
	box-shadow: 1px 2px rgb(143, 139, 139);
    position: fixed;
    top: 40%;
    left: 0;
    list-style: none;
    padding-left: 0;
    z-index: 10;
    margin: 0;
    -webkit-transition: left 0.25s ease-in-out;
    transition: left 0.25s ease-in-out;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -ms-flex-direction: column;
    flex-direction: column;
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
  


  <div class="container-fluid fh5co-home-banner">
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
          

	
	  
 

  
  
    
	  
	  
      <div class="container recent a" id="activity">
	 <div class="col-md-12" style="background-color:#fa86c4 !important; height:100px; "><h1 style="color:black; font-family:algerian; margin-left:40%; padding-top:20px;"> SCHOOL</h1></div>
	  
        <div class="row">
          <!-- <h2 style="font-family:algerian; color:black;">Achievement</h2> -->
          <div class="owl-carousel owl-carousel2 owl-theme">
            <div>
              <div class="card"> <img class="card-img" src="assets/img/ac.jpg" alt="">
                <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a>
                  <div class="bottom-text">
                    <h5 class="card-title" style="font-family:algerian;">UKG<h5>
                    <p class="card-text">Samtolan Aat</p>
                  </div>
                </div>
              </div>
            </div>
            <div>
              <div class="card"> <img class="card-img" src="assets/img/ac2.jpg" alt="">
                <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a>
                  <div class="bottom-text">
                 <h5 class="card-title" style="font-family:algerian;">UKG</h5>
                    <p class="card-text">HADUV</p>
                  </div>
                </div>
              </div>
            </div>
            <div>
              <div class="card"> <img class="card-img" src="assets/img/ac3.jpg" alt="">
                <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a>
                  <div class="bottom-text">
                     <h5 class="card-title" style="font-family:algerian;">MHPS Bugate Alur</h5>
                    <p class="card-text">PATRIOTIC SONG</p>
                  </div>
                </div>
              </div>
            </div>
            <div>
              <div class="card"> <img class="card-img" src="assets/img/ac4.jpg" alt="">
                <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a>
                  <div class="bottom-text">
                    <h5 class="card-title" style="font-family:algerian;">MHPS Bugate Alur</h5>
                    <p class="card-text">SHOT-PUT</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  
	  
      <div class="container recent a" id="activity">
	  	 <div class="col-md-12" style="background-color:#fa86c4 !important; height:100px; "><h1 style="color:black; font-family:algerian; margin-left:40%; padding-top:20px;"> HIGH SCHOOL</h1></div>

        <div class="row">
          <!-- <h2 style="font-family:algerian; color:black;">Achievement</h2> -->
          <div class="owl-carousel owl-carousel2 owl-theme">
            <div>
              <div class="card"> <img class="card-img" src="assets/img/ac9.jpg" alt="">
                <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a>
                  <div class="bottom-text">
                    <h5 class="card-title" style="font-family:algerian;">PVK Nangnur[KS]</h5>
                    <p class="card-text">KABBADI</p>
                  </div>
                </div>
              </div>
            </div>
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
          </div>
        </div>
      </div>
    </div>
  </div>
  
  
  
	  
      <div class="container recent a" id="activity">
        <div class="row">
          <!-- <h2 style="font-family:algerian; color:black;">Achievement</h2> -->
          <div class="owl-carousel owl-carousel2 owl-theme">
            <div>
              <div class="card"> <img class="card-img" src="assets/img/ac16.jpg" alt="">
                <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a>
                  <div class="bottom-text">
                    <h5 class="card-title" style="font-family:algerian;">PVK Nangnur[KS]</h5>
                    <p class="card-text">Top 2 Student</p>
                  </div>
                </div>
              </div>
            </div>
            <div>
              <div class="card"> <img class="card-img" src="assets/img/ac11.jpg" alt="">
                <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a>
                  <div class="bottom-text">
                 <h5 class="card-title" style="font-family:algerian;">PVK Nangnur[KS]</h5>
                    <p class="card-text">Singing</p>
                  </div>
                </div>
              </div>
            </div>
            <div>
              <div class="card"> <img class="card-img" src="assets/img/ac12.jpg" alt="">
                <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a>
                  <div class="bottom-text">
                     <h5 class="card-title" style="font-family:algerian;">PVK Nangnur[KS]</h5>
                    <p class="card-text">Shot-Put</p>
                  </div>
                </div>
              </div>
            </div>
            <div>
              <div class="card"> <img class="card-img" src="assets/img/ac13.jpg" alt="">
                <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a>
                  <div class="bottom-text">
                    <h5 class="card-title" style="font-family:algerian;">PVK Nangnur[KS]</h5>
                    <p class="card-text">Volly-ball</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  
  
  
	  
      <div class="container recent a" id="activity">
        <div class="row">
          <!-- <h2 style="font-family:algerian; color:black;">Achievement</h2> -->
          <div class="owl-carousel owl-carousel2 owl-theme">
            <div>
              <div class="card"> <img class="card-img" src="assets/img/ac14.jpg" alt="">
                <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a>
                  <div class="bottom-text">
                    <h5 class="card-title" style="font-family:algerian;">PVK Nangnur[KS]</h5>
                    <p class="card-text">Teachers Day</p>
                  </div>
                </div>
              </div>
            </div>
            <div>
              <div class="card"> <img class="card-img" src="assets/img/ac15.jpg" alt="">
                <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a>
                  <div class="bottom-text">
                 <h5 class="card-title" style="font-family:algerian;">PVK Nangnur[KS]</h5>
                    <p class="card-text">Cricket</p>
                  </div>
                </div>
              </div>
            </div>
            <div>
              <div class="card"> <img class="card-img" src="assets/img/ac10.jpg" alt="">
                <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a>
                  <div class="bottom-text">
                     <h5 class="card-title" style="font-family:algerian;">PVK Nangnur[KS]</h5>
                    <p class="card-text">Kho-Kho</p>
                  </div>
                </div>
              </div>
            </div>
            <div>
              <!-- <div class="card"> <img class="card-img" src="assets/img/ac17.jpg" alt=""> -->
                <!-- <div class="card-img-overlay"> <a href="#"><img src="assets/img/heart.png" class="heart" alt="heart icon"></a> -->
                  <!-- <div class="bottom-text"> -->
                    <!-- <h5 class="card-title" style="font-family:algerian;">PVK Nangnur[KS]</h5> -->
                    <!-- <p class="card-text">Ka</p> -->
                  <!-- </div> -->
                <!-- </div> -->
              <!-- </div> -->
            </div>
          </div>
        </div>
      </div>
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
            <p class="text-justify" style="font-family:Goudy Old Style;">Hi there! I’m Bhakti, a web developer with a strong passion for technology, design, and innovation. Currently, 
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
  
  
  
  
  
  
  
  
  
  <footer class="container-fluid p-0 pr-0">
    
    <div class="copy pt-4 pb-4" >
      <p><a href="https://freehtml5.co/" target="_blank"> &copy; 2003</a>  &nbsp;  |  &nbsp; Design by <a href="https://freehtml5.co/" target="_blank">Bhakti Bhosale</a> &nbsp; &nbsp;  </p>
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