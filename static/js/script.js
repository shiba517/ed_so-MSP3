$(document).ready(function() {
    // Navbar actions for mobile and tablet devices
    $('.sidenav').sidenav();

    // A modal opens up on the screen; Can be found in profile.html and chosen_recipe.html
    $('.modal').modal();
    
    // A button that is when hovered or clicked on, more buttons appear. Can be found in chosen_recipe.html
    $('.fixed-action-btn').floatingActionButton();
});