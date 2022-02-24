<?php 

session_start();

if (!isset($_SESSION['username'])) {
    header("Location: indexlogin.php");
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>
</head>
<body>
<!--Navbar-->
    <nav class="navbar navbar-expand-lg navbar-light bg-dark" data-spy="affix" data-offset-top="197">
        <div class="container-fluid" >
          <a class="navbar-brand" style="color: #fff" href="#">Face Mask Detector<i class="fas fa-viruses px-2"></i></a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNavDropdown">
            <ul class="navbar-nav m-auto" style="margin-left: 20px; padding-right: 50px;">
              <li class="nav-item">
                <a class="nav-link active" style="color: #fff" aria-current="page" href="../index.php">HOME <i class="fas fa-home px-1"></i></a>
              </li>
              <li class="nav-item">
                <a class="nav-link" style="color: #fff" href="../Join Our Team/join_page.html">JOIN OUR TEAM<i class="fas fa-users-cog px-2"></i></a>
              </li>
              <li class="nav-item">
                <a class="nav-link" style="color: #fff" href="https://www.timesnownews.com/">NEWS<i class="fas fa-newspaper px-2"></i></a>
              </li>
              <li class="nav-item">
                <a class="nav-link" style="color: #fff" href="../contact.php">CONTACT US<i class="fas fa-address-book px-2"></i></a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
  <!--Navbar-->
    <?php echo "<h1>Welcome " . $_SESSION['username'] . "</h1>"; ?>
    <a href="logout.php">Logout</a>

</body>
</html>