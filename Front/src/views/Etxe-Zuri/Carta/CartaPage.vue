<template>
  <div
    class="carta"
    :style="{
      backgroundImage: `url(${background.background})`,
      color: background.color,
    }"
  >
    <div class="personalData">
      <h3>TEL: 674 563 059</h3>
      <h3>SIXTA BARRENETXEA 21 GALDAKAO</h3>
      <span>(Atendemos reservas telefónicas de 9:00 a 23:00)</span>
    </div>
    <div id="cartaImage">
      <div class="cartaImg">
        <img src="~@/assets/logos-Etxe-Zuri/restaurant.png" alt="" />
      </div>
      <h1>ETXE ZURI</h1>
      <div class="cartaImg">
        <img src="~@/assets/logos-Etxe-Zuri/restaurant.png" alt="" />
      </div>
    </div>
    <div class="grid-container">
      <br />
      <div class="hamburguesas">
        <div class="imgcard">
          <img src="~@/assets/logos-Etxe-Zuri/logo-burguer.png" alt="" />
        </div>
        <h3 class="categorias">HAMBURGUESAS</h3>
        <div class="category-item" v-for="item in carta" :key="item">
          <itemCarta v-if="item.category == 'Hamburguesas'" :item="item" />
        </div>
      </div>
      <br />
      <div class="sandwitch">
        <div class="imgcard">
          <img src="~@/assets/logos-Etxe-Zuri/logo-sandwich.png" alt="" />
        </div>
        <h3 class="categorias">SANDWITCH</h3>
        <div class="category-item" v-for="item in carta" :key="item">
          <itemCarta v-if="item.category == 'Sandwitch'" :item="item" />
        </div>
      </div>
      <br />
      <div class="bocadillos">
        <div class="imgcard">
          <img src="~@/assets/logos-Etxe-Zuri/logo-bocadillo.png" alt="" />
        </div>
        <h3 class="categorias">BOCADILLOS</h3>
        <div class="category-item" v-for="item in carta" :key="item">
          <itemCarta v-if="item.category == 'Bocadillos'" :item="item" />
        </div>
      </div>
      <br />
      <div class="raciones">
        <div class="imgcard">
          <img src="~@/assets/logos-Etxe-Zuri/logo-empanada.png" alt="" />
        </div>
        <h3 class="categorias">RACIONES</h3>
        <div class="category-item" v-for="item in carta" :key="item">
          <itemCarta v-if="item.category == 'Raciones'" :item="item" />
        </div>
      </div>
      <br />
      <div class="tortillas">
        <div class="imgcard">
          <img src="~@/assets/logos-Etxe-Zuri/logo-tortilla.png" alt="" />
        </div>
        <h3 class="categorias">TORTILLAS</h3>
        <div class="category-item" v-for="item in carta" :key="item">
          <itemCarta v-if="item.category == 'Tortillas'" :item="item" />
        </div>
      </div>
    </div>
    <div class="chopito">
      <div>
        <img src="~@/assets/logos-Etxe-Zuri/logo-calamar.png" alt="" />
      </div>
      <h3>TXOPITOS A 5.00€</h3>
      <span>Sabados, Domingos y festivos de 11:00 a 15:30</span>
    </div>
  </div>
</template>

<script>
import api from "@/services/api";
import itemCarta from "./itemCarta.vue";
export default {
  name: "Carta",
  components: {
    itemCarta,
  },
  data() {
    return {
      carta: [],
      dataTheme: [],
      theme: "Pared_blanca",
    };
  },
  computed: {
    background() {
      let result = this.dataTheme.filter((them) => {
        if (them.id == this.theme) {
          console.log("1");
          return them;
        }
      });

      let xx = result[0];
      console.dir(xx);
      return xx;
    },
  },
  methods: {
    async getCartas() {
      this.carta = await api.getCartas();
    },
    async getThemes(theme) {
      this.dataTheme = await api.getThemes(theme);
    },
  },

  async created() {
    this.getCartas();
    this.getThemes();
  },
};
</script>

<style scoped>
.grid-container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 1.3em;
}
.personalData {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr;
}
.carta {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 1.3rem;
}
#cartaImage {
  display: flex;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr;
  margin-left: 450px;
  padding-top: 30px;
}
img {
  margin-top: 20px;
  width: 90px;
  margin-right: 30px;
}
h1 {
  margin-top: 40px;
}
h3 {
  text-decoration: double underline;
}
.categorias {
  text-decoration: double underline;
}
.cartaspan {
  text-align: center;
  margin: 10px;

  font-size: 26px;
}
span.categorias {
  font-size: 25px;
  margin-bottom: 10px;
}

.hamburguesas {
  text-align: left;
  margin: 60px 0px 0px -243px;
}
.sandwitch {
  text-align: left;
  margin: 60px 47px 0px -240px;
}
.bocadillos {
  text-align: left;
  margin: -130px 36px 0px -239px;
}
.raciones {
  text-align: left;
  margin: -95px 36px 0px -239px;
}
.tortillas {
  text-align: left;
  margin: -250px -88px 0px -243px;
}
.itemCarta {
  text-align: center;
}
.chopito {
  padding-bottom: 30px;
}

@media screen and (max-width: 740px) {
  .grid-container {
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: 1fr;
    gap: 1.3em;
  }
  .personalData {
    display: grid;
    grid-template-columns: 1fr;
  }
  #cartaImage {
    justify-content: center;
    margin: 0 auto;
    font-size: 10px;
  }
  .cartaImg {
    display: none;
  }
  h1 {
    margin-top: 88px;
    padding-right: 130px;
    font-size: 30px;
  }
  .categorias {
    text-decoration: double underline;
  }
  .hamburguesas {
    text-align: left;
    margin: 40px 9px 0px -3px;
  }
  .sandwitch {
    text-align: center;
    margin: 60px 47px 0 0;
  }
  .bocadillos {
    text-align: center;
    margin: -170px 9px 0px -3px;
  }
  .raciones {
    text-align: center;
    margin: -76px 9px 0px -3px;
  }
  .tortillas {
    text-align: center;
    margin: -276px 9px 0px -3px;
  }
}

@media screen and (max-width: 1024px) {
  .personalData {
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: 1fr;
  }
  #cartaImage {
    display: flex;
    margin-left: 140px;
  }
  h1 {
    margin-top: 45px;
    margin-right: 5px;
  }
  .categorias {
    text-decoration: double underline;
  }
  .grid-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr;
    margin-right: 100px;
  }
  .hamburguesa {
    text-align: left;
  }
  .sandwitch {
    text-align: left;
    margin-bottom: 200px;
  }
  .bocadillos {
    text-align: left;
    margin-bottom: 140px;
  }
  .raciones {
    text-align: left;
    margin-bottom: 300px;
  }
  .tortillas {
    text-align: left;
    margin-bottom: 50px;
  }
  .chopito {
    margin-bottom: 30px;
  }
}
</style>
