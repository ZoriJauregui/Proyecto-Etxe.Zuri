<template>
  <div class="itemcard">
    <li v-for="product in item.products" :key="product">
      <span>{{ product.product_id }}</span>
      <span>{{ product.ingredients }}</span>
      <span>Precio: {{ product.price }}</span>
    </li>
  </div>
</template>

<script>
export default {
  name: "itemCarta",
  props: {
    item: {
      propType: Array,
      required: true,
    },
  },
  data() {
    return {};
  },

  methods: {},
};
</script>

<style>
.itemcard {
  text-align: row;
}
span {
  margin-left: 10px;
}
</style>
