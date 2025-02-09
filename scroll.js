document.getElementById('scrollButton').addEventListener('click', function() { 
    window.scrollTo({ 
        top: document.body.scrollHeight, 
        behavior: 'smooth' // This makes the scrolling smooth 
    }); 
});