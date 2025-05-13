<script setup>
import {reactive, ref, watch} from 'vue'

var products = reactive([
  {
    name: 'Caran D`Ache Neocolor - Tonos Fríos',
    price: '21,05 €',
    stock: 5,
    availeability: true,
    image: new URL('@/assets/caran-dache-neocolor-ii-caja-metalica-seleccion-beya-rebai-10-ceras-acuarelables-tonos-frios.jpg', import.meta.url).href
  },
  {
    name: 'Caran D`Ache Neocolor - Tonos Cálidos',
    price: '21,05 €',
    stock: 5,
    availeability: true,
    image: new URL('@/assets/caran-dache-neocolor-ii-caja-metalica-seleccion-beya-rebai-10-ceras-acuarelables-tonos-calidos.jpg', import.meta.url).href
  },
  {
    name: 'Silver Bristlon Pincel Redondo Mango Serie 1900',
    price: '9,20 €',
    stock: 15,
    availeability: true,
    image: new URL('@/assets/silver-bristlon-pincel-redondo-mango-largo-serie-1900.jpg', import.meta.url).href
  },
  {
    name: 'Etchr The Perfect Sketchbook 300G 100% Algodón',
    price: '35,33 €',
    stock: 6,
    availeability: true,
    image: new URL('@/assets/etchr-the-perfect-sketchbook-300-g-100-algodon.jpg', import.meta.url).href
  },
  {
    name: 'Rembrandt Caja Óleo Master 24 Tubos',
    price: '330,00 €',
    stock: 8,
    availeability: true,
    image: new URL('@/assets/rembrandt-caja-oleo-master-24-tubos.jpg', import.meta.url).href
  }

]);

const increaseStock = (product) => {
  product.stock++;
};

const decreaseStock = (product) => {
  if (product.stock > 0) {
    product.stock--;
  }
};

watch(
  () => products.map(p => p.stock),
  () => {
    products.forEach(product => {
      product.availeability = product.stock > 0;
    });
  },
  { deep: true }
);
</script>

<template>
  <v-layout>
    <v-app-bar :elevation="2" rounded color="grey-darken-4">
      <v-app-bar-title>Control de Inventario</v-app-bar-title>
    </v-app-bar>

    <v-main>
      <v-container class="bg-surface-variant lg-6"  style="min-height: 100vh;">
        <v-row>
          <v-col v-for="product in products" :key="product.id" cols="12" sm="6" md="4" lg="3">
            <v-card class="mx-auto" :color="product.availeability ? 'grey-darken-4' : 'red-darken-2'">
              <v-img
                height="200px"
                :src= 'product.image'
                cover
              ></v-img>

              <v-card-title> {{ product.name }} </v-card-title>
              <v-card-subtitle> Precio: {{ product.price }} </v-card-subtitle>
              <v-card-subtitle> 
                <v-btn icon size="x-small" @click="decreaseStock(product)">
                  -
                </v-btn>
                Stock: {{ product.stock }} 
                <v-btn icon size="x-small" @click="increaseStock(product)">
                  +
                </v-btn>
              </v-card-subtitle>

            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-layout>
</template>

<style scoped>

</style>
