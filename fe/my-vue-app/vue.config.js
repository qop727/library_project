const { defineConfig } = require("@vue/cli-service");

module.exports = defineConfig({
  publicPath: "/",
  devServer: {
    host: "0.0.0.0", // listen on all network interfaces
    port: 8080,
  },
  transpileDependencies: true,
});
