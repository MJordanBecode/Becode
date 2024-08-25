(function() {
    document.getElementById('guess-form')?.addEventListener("submit", compareUserGuess);

    function compareUserGuess(event: Event) {
        event.preventDefault();

        const secretNumber = generateSecretNumber();
        const userNumber = (document.getElementById('guess') as HTMLInputElement).value;
        const userNumberAsNumber = parseInt(userNumber, 10);

        if (secretNumber === userNumberAsNumber) {
            alert(`Awesome! Your number ${userNumber} was correct. You can be named many things, hungry not being one of them.`);
        } else {
            alert(`Bummer... You guessed ${userNumber} and the secret number was ${secretNumber}.`);
        }
    }

    function generateSecretNumber(): number {
        const secretNumber = getRandomArbitrary(1, 22);

        return secretNumber;
    }

    function getRandomArbitrary(min: number, max: number): number {
        return Math.round(Math.random() * (max - min) + min);
    }
})();
