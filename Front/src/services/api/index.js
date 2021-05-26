export default {
  async get(url) {
    const response = await fetch(url, { method: "GET" });
    if (response.ok) {
      return await response.json();
    } else {
      console.error("Error", response);
    }
  },
  async post(url, data) {
    return await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
  },

  async getCartas() {
    return await this.get("/api/Etxe-Zuri/Carta");
  },
  async getThemes() {
    return await this.get("/api/Etxe-Zuri/Theme");
  },
};
