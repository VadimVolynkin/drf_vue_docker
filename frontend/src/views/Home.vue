<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>Vendor</th>
          <th>Model</th>
          <th>Year</th>
          <th>Volume</th>
      </tr>
      </thead>
      <tbody>
        <tr v-for="car in cars" :key="car.id">
          <td>{{ car.vendor }}</td>
          <td>{{ car.model }}</td>
          <td>{{ car.year }}</td>
          <td>{{ car.volume }}</td>
        </tr>
      </tbody>
    </table>

    <input placeholder="vendor" v-model="currentCar.vendor">
    <input placeholder="model" v-model="currentCar.model">
    <input placeholder="year" v-model.number="currentCar.year">
    <input placeholder="volume" v-model.number="currentCar.volume">
    <button @click="createCar()">Create</button>

  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      cars:[],
      currentCar:{},
    }
  },


  async created() {

    // get cars from backend in first time
    this.fetchCars()
  },

  methods: {

    // create function GET cars from backend
    async fetchCars() {
      const response = await fetch('http://127.0.0.1:8000/api/cars/')
      this.cars = await response.json()
    },

    // create function POST new car
    async createCar() {
      const response = await fetch('http://127.0.0.1:8000/api/cars/' , {
        method: "POST",
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.currentCar)
      })

      // check status after POST and show alert with response data
      if (response.status !== 201) {
        alert(JSON.stringify(await response.json(), null, 2))
      } else {
      // clear createform on frontend after POST
      this.currentCar.vendor = ''
      this.currentCar.model = ''
      this.currentCar.year = ''
      this.currentCar.volume = ''
      }

      // get cars with new added car from backend after backend-validation
      await this.fetchCars()
    }
  }
}
</script>
