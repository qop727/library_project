<!-- FE Vue.js for library project. -->

<template>
  <div id="app">
    <h1>My Library</h1>

    <!-- Form for saving the book. -->
    <div>
      <h2>Add a Book</h2>
      <input v-model="author" placeholder="Author" /><br />
      <input v-model="title" placeholder="Title" />
      <button @click="addBook">Save</button>
    </div>

    <!-- Form for searching the book. -->
    <div>
      <h2>Search Books</h2>
      <input v-model="keyword" placeholder="Enter keyword" />
      <button @click="searchBooks">Search</button>
    </div>

    <!-- Form for searching the book. -->
    <div>
      <h2>Delete Books by ID</h2>
      <input v-model="id" placeholder="Enter ID" />
      <button @click="deleteBooks">Delete</button>
    </div>

    <!-- Status messages. -->
    <div>
      <p :style="{ color: statusColor }">{{ statusMessage }}</p>
    </div>

    <!-- List of found books. -->
    <div>
      <h2>List of Books</h2>
      <ul>
        <li v-for="book in books" :key="book.id">
          {{ book.id }} - {{ book.author }} - {{ book.title }}
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
    const id = ref("");
    const books = ref<Book[]>([]);
    const statusMessage = ref("");
    const statusColor = ref("black");

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
        statusColor.value = "green";
        author.value = "";
        title.value = "";
      } catch (error) {
        statusMessage.value = "Error adding book";
        statusColor.value = "red";
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
        statusColor.value = "green";
      } catch (error) {
        statusMessage.value = "Error searching books";
        statusColor.value = "red";
      }
    };

    const deleteBooks = async () => {
      try {
        await axios.delete("http://192.168.0.234:5000/api/delete", {
          params: { id: id.value },
        });
        statusMessage.value = "Succesfully deleted";
        statusColor.value = "green";
      } catch (error) {
        statusMessage.value = "Error deleting books";
        statusColor.value = "red";
      }
    };

    return {
      author,
      title,
      keyword,
      id,
      books,
      statusMessage,
      statusColor,
      addBook,
      searchBooks,
      deleteBooks,
    };
  },
});
</script>

<style>
#app {
  max-width: 1024px;
  margin: 0 auto;
  padding: 150px;
  font-family: Lexend, sans-serif;
  background-image: url("backgroung.png");
  background-position: center;
  background-repeat: no-repeat;
  color: rgb(0, 137, 161);
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
