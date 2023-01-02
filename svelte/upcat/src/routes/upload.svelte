<script>
    import { onMount } from "svelte";
    import { createEventDispatcher } from "svelte";
  
    const dispatch = createEventDispatcher();
  
    function handleSubmit(event) {
      event.preventDefault();
  
      // Get the file input element
      const fileInput = event.target.elements.file;
      const file = fileInput.files[0];
  
      // Create a FormData object to send the file in the request body
      const formData = new FormData();
      formData.append("file", file);
  
      // Make the POST request to the API
      fetch("http://localhost:8000/files/", {
        method: "POST",
        body: formData,
      })
        .then((response) => response.json())
        .then((data) => {
          dispatch("fileUploaded", data);
        })
        .catch((error) => {
          console.error(error);
        });
    }
  </script>
  
  <form on:submit|preventDefault={handleSubmit}>
    <input type="file" name="file" />
    <button type="submit">Upload</button>
  </form>
  