//VARIABLES
let currentUserName = '';
let currentQuote = {};
let interactionCount = 0;

// Get HTML elements
const userName = document.getElementById('userName');
const submitBtn = document.getElementById('submitBtn');
const userForm = document.getElementById('userForm');
const quoteSection = document.getElementById('quoteSection');
const quoteCard = document.getElementById('quoteCard');
const quoteText = document.getElementById('quoteText');
const characterText = document.getElementById('characterText');
const sourceText = document.getElementById('sourceText');
const nextBtn = document.getElementById('nextBtn');
const interactionCountDisplay = document.getElementById('interactionCount');
const viewHistoryBtn = document.getElementById('viewHistoryBtn');
const historyContent = document.getElementById('historyContent');
const historyList = document.getElementById('historyList');

//FUNCTIONS

function handleUserSubmit(event) {  
  event.preventDefault(); //Stop form from submitting 
  
  const name = userName.value.trim();
  // Validate that name is not empty
  if (name === '') {
    alert('Please enter your name!');
    return;
  }
  
  // Store the name
  currentUserName = name;
  
  // Hide form, show quote section
  userForm.style.display = 'none';
  quoteSection.style.display = 'block';
  
  // Fetch the first quote
  fetchQuote();
}

function fetchQuote() {
  fetch('http://localhost:5000/api/quotes')
    .then(response => response.json())
    .then(quote => {
      // Store the quote
      currentQuote = quote;
      
      // Display the quote
      displayQuote(quote);
      
      // Log this interaction
      logInteraction('quote_viewed');
    })
    .catch(error => {
      console.error('Error fetching quote:', error);
      quoteText.textContent = 'Error loading quote. Make sure Flask server is running!';
    });
}

function displayQuote(quote) {
  quoteText.textContent = `"${quote.quote}"`;
  characterText.textContent = `— ${quote.character}`;
  sourceText.textContent = `${quote.source}`;
  
  // Update counter
  interactionCount++;
  interactionCountDisplay.textContent = `Quotes viewed: ${interactionCount}`;
}

function logInteraction(action) {
  const interactionData = {
    name: currentUserName,
    action: action,
    quote: currentQuote.quote,
    character: currentQuote.character,
    source: currentQuote.source,
  };
  
  fetch('http://localhost:5000/api/interaction', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(interactionData)
  })
    .then(response => response.json())
    .then(data => {
      console.log('Interaction logged:', data);
    })
    .catch(error => {
      console.error('Error logging interaction:', error);
    });
}


//LISTENERS

// When user clicks "Start" button
submitBtn.addEventListener('click', handleUserSubmit);

// When user clicks "Get Another Quote" button
nextBtn.addEventListener('click', fetchQuote);