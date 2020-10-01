<template>
    <div>
        <h1>{{ car.model }}</h1>
        <h3>{{ car.vendor }}</h3>
        <h3>{{ car.year }}</h3>
        <h3>{{ car.volume }}</h3>

        <div v-if="isUpdating">
            <input v-model="currentCar.vendor" />
            <input v-model="currentCar.model" />
            <input v-model="currentCar.year" />
            <input v-model="currentCar.volume" />
            <button @click="confirmUpdateCar(car)">Confirm</button>
            <button @click="cancelUpdateCar()">Cancel</button>
        </div>
        <div v-else>
            <button @click="updateCar(car)">Update</button>
            <button @click="removeCar()">Delete</button>
        </div>
    </div>
</template>

<script>
import axios from "axios";
export default {
    name: "Car",
    data() {
        return {
            car: {},
            id: this.$route.params.id,
            url: `http://127.0.0.1:8000/api/cars/${this.$route.params.id}/`,
            currentCar: {},
            isUpdating: false,
        };
    },
    created() {
        // get Car in the first time
        this.getCar();
    },
    methods: {
        // get Car from backend
        async getCar() {
            await axios
                .get(this.url)
                .then((response) => {
                    this.car = response.data;
                })
                .catch((error) => alert(error));
        },

        async updateCar() {
            await axios.get(this.url).then((response) => {
                this.currentCar = response.data;
            });
            this.isUpdating = true;
        },

        async confirmUpdateCar() {
            await axios
                .put(this.url, this.currentCar)
                .then(() => {
                    // get Car after backend-validation
                    this.getCar();
                })
                .catch((error) => alert(error));
            // switch updating status
            this.isUpdating = false;
            // clear form
            this.currentCar = {};
        },

        async cancelUpdateCar() {
            this.currentCar = {};
            this.isUpdating = false;
        },

        async removeCar() {
            await axios
                .delete(this.url)
                .then(() => {
                    // got to Home
                    this.$router.push({ name: "Home" });
                })
                .catch((error) => alert(error));
        },
    },
};
</script>

<style>
</style>