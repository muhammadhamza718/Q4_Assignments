document.addEventListener('DOMContentLoaded', function() {
    // Like Button Functionality
    const likeButtons = document.querySelectorAll('.car-card__like-button');

    likeButtons.forEach(button => {
        button.addEventListener('click', () => {
            button.classList.toggle('bxs-heart'); // Filled heart
            button.classList.toggle('bx-heart'); // Regular heart
            button.classList.toggle('liked');
        });
    });

    // Search Form Swap Functionality
    const swapButton = document.querySelector('.search__swap-button');
    const pickupLocation = document.getElementById('pickup-location');
    const dropoffLocation = document.getElementById('dropoff-location');
    const pickupDate = document.getElementById('pickup-date');
    const dropoffDate = document.getElementById('dropoff-date');
    const pickupTime = document.getElementById('pickup-time');
    const dropoffTime = document.getElementById('dropoff-time');

    swapButton.addEventListener('click', () => {
        // Swap values
        [pickupLocation.value, dropoffLocation.value] = [dropoffLocation.value, pickupLocation.value];
        [pickupDate.value, dropoffDate.value] = [dropoffDate.value, pickupDate.value];
        [pickupTime.value, dropoffTime.value] = [dropoffTime.value, pickupTime.value];
    });

    // Show More Cars Functionality
    const showMoreButton = document.querySelector('.car-list__show-more-button');
    const hiddenCards = document.querySelectorAll('.car-list .car-card.hidden');
    const recommendationList = document.getElementById('recommendation-list');
    const showMoreContainer = document.querySelector('.car-list__show-more');

    showMoreButton.addEventListener('click', () => {
        hiddenCards.forEach(card => {
            card.classList.remove('hidden');
        });
        recommendationList.classList.remove('hidden');
        showMoreContainer.classList.add('hidden');
    });
});
