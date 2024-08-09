 // JavaScript for dropdown menu in the left nav
 var dropdowns = document.getElementsByClassName("dropdown-btn");
 for (var i = 0; i < dropdowns.length; i++) {
     dropdowns[i].addEventListener("click", function() {
         this.classList.toggle("active");
         var dropdownContent = this.nextElementSibling;
         dropdownContent.classList.toggle("show");
         if (dropdownContent.style.display === "block") {
             dropdownContent.style.display = "none";
         } else {
             dropdownContent.style.display = "block";
         }
     });
 }
