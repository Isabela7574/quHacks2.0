// JavaScript logic (script.js)
document.getElementById("madLibsForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form from submitting and refreshing page
  
    // Get user input
    let noun = document.getElementById("noun").value;
    let adjective1 = document.getElementById("adjective1").value;
    let adjective2 = document.getElementById("adjective2").value;
    let adjective3 = document.getElementById("adjective3").value;
    let adjective4 = document.getElementById("adjective4").value;
    let verb1 = document.getElementById("verb1").value;
    let verb2 = document.getElementById("verb2").value;
    let time = document.getElementById("time").value;
  
    // Create the story
    let story = "It was a cold yet sunny December day at " + adjective1 + " QuHacks. " + "I woke up at " + time + " to check my discord dms to see if my bestie was gonna pull up. I relized I was a bit pressed for time so I grabed my " + noun + " that my grandma got me for my birthday and left the house. Fortunately, the " + noun + " helped me to " + verb1 + " the car. I entered through the " + adjective2 + " doors and met some " + adjective3 + " people trying to " + verb2 + " it up. Finally, I met up with the homies and began coding our " + adjective4 + " game <i>Fortress.</i>";
    // Display the story";
    
    // 
    // Display the story
    document.getElementById("story").innerHTML = story;
  });