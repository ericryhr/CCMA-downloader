<script lang="ts">
	let userInput = '';
  
	const handleSubmit = () => {
	  alert(`You entered: ${userInput}`);
	};
</script>
  
<div>
    <h1>Text Form</h1>

    <form on:submit|preventDefault={handleSubmit}>
        <label for="textInput">Enter Text:</label>
        <input
            type="text"
            id="textInput"
            bind:value={userInput}
            placeholder="Type something..."
        />

        <button type="submit">Confirm</button>
    </form>
</div>

<style>
	h1 {
		width: 100%;
	}
</style>