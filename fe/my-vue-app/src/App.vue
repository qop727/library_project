<!-- FE Vue.js for library project. -->

<template>
  <div id="app">
    <h1>Book Manager</h1>

    <!-- Form for saving the book. -->
    <div>
      <h2>Add a Book</h2>
      <input v-model="author" placeholder="Author" />
      <input v-model="title" placeholder="Title" />
      <button @click="addBook">Save</button>
    </div>

    <!-- Formu for searching the book. -->
    <div>
      <h2>Search Books</h2>
      <input v-model="keyword" placeholder="Enter keyword" />
      <button @click="searchBooks">Search</button>
    </div>

    <!-- Status messages. -->
    <div>
      <p>{{ statusMessage }}</p>
    </div>

    <!-- List of found books. -->
    <div>
      <h2>Books</h2>
      <ul>
        <li v-for="book in books" :key="book.id">
          {{ book.author }} - {{ book.title }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import axios from "axios";

interface Book {
  id: number;
  author: string;
  title: string;
}

export default defineComponent({
  name: "App",
  setup() {
    const author = ref("");
    const title = ref("");
    const keyword = ref("");
    const books = ref<Book[]>([]);
    const statusMessage = ref("");

    const addBook = async () => {
      try {
        const response = await axios.post(
          "http://192.168.0.234:5000/api/book",
          {
            author: author.value,
            title: title.value,
          }
        );
        statusMessage.value = response.data.message;
        author.value = "";
        title.value = "";
      } catch (error) {
        statusMessage.value = "Error adding book";
      }
    };

    const searchBooks = async () => {
      try {
        const response = await axios.get(
          "http://192.168.0.234:5000/api/search",
          {
            params: { keyword: keyword.value },
          }
        );
        books.value = response.data;
        statusMessage.value = "Search completed";
      } catch (error) {
        statusMessage.value = "Error searching books";
      }
    };

    return {
      author,
      title,
      keyword,
      books,
      statusMessage,
      addBook,
      searchBooks,
    };
  },
});
</script>

<style>
#app {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Lexend, sans-serif;
  background-image: url("backgroung.png");
  background-blend-mode: difference;
  background-position: center;
  background-repeat: no-repeat;
}
input {
  margin: 5px;
  padding: 8px;
  font-size: 14px;
}
button {
  margin: 5px;
  padding: 8px 16px;
  font-size: 14px;
}
</style>
