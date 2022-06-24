<template>
  <v-container class="fluid">
    <v-row justify="center">
      <v-carousel v-model="model" height="200" class="background">
        <v-carousel-item v-for="(item, i) in items" :key="i" :src="item.src">
        </v-carousel-item>
      </v-carousel>
    </v-row>

    <v-row style="margin-top: 15px">
      <v-col cols="7.5" style="margin-right: 15px">
        <v-row
          class="row"

          justify="center"
          style="background-color: rgb(87, 168, 87)"
        >
          <datepicker
            v-model="picked"
            @update:modelValue="getMatchesByDay"
            style="height: 47px; text-align: center"
          />
        </v-row>

        <v-row
          justify="center"
          class="row"
          style="margin-top: 10px; border-radius: 10px"
        >
          <v-list style="width: 98%">
            <v-list-item
              v-for="(item, i) in matches"
              :key="i"
              :value="item"
              active-color="primary"
              rounded="xl"
            >
              <v-list-item-content style="width: 100%">
                <v-row class="border">
                  <v-col cols="2" style="width: 100%">
                    <v-row style="margin-bottom: 10px" class="borderRow">
                      <v-img
                        :src="item.home_logo || defaultURL"
                        height="30"
                        width="30"
                      ></v-img>
                    </v-row>
                    <v-row class="borderRow" justify="center">
                      {{ item.home_name }}
                    </v-row>
                  </v-col>
                  <v-col cols="2" class="score"> {{ item.home_goal }} </v-col>
                  <v-col cols="4" style="margin-top: 10px">
                    <v-row justify="center"> {{ item.start_time }}</v-row>
                    <v-row justify="center" class="borderCol"> : </v-row>
                    <v-row class="borderRow" justify="center">
                      {{ item.place }}</v-row
                    >
                  </v-col>
                  <v-col cols="2" class="score"> {{ item.away_goal }} </v-col>
                  <v-col cols="2">
                    <v-row style="margin-bottom: 10px" class="borderRow">
                      <v-img
                        :src="item.away_logo || defaultURL"
                        height="30"
                        width="30"
                      ></v-img>
                    </v-row>
                    <v-row class="borderRow" justify="center">
                      {{ item.away_name }}</v-row
                    >
                  </v-col>
                </v-row>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-row>
      </v-col>

      <v-col cols="4" class="row" style="margin-top: 21px; max-height: 500px">
        <v-row justify="center" class="colorrank">
          <v-tabs background-color="green">
            <v-tab
              v-for="league in leagues"
              :key="league.id"
              :value="league.id"
              @click="changeTab(league.id)">
                {{ league.name }}
              </v-tab
            >
          </v-tabs>
        </v-row>

        <v-row justify="center">
            <v-table class="clubranking">
              <tbody>
                <tr v-for="(item, index) in clubs" :key="item.id">
                  <td>{{ index + 1 }}</td>
                  <td>{{ item.name }}</td>
                  <td>{{ item.points }}</td>
                </tr>
              </tbody>
            </v-table>         
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { useStore } from "./store.ts";
import Datepicker from "vue3-datepicker";
import { ref, onMounted } from "vue";
import Laliga from "../assets/Laliga.png";
import EPL from "../assets/EPL.png";
import SerieA from "../assets/SerieA.png";

export default {
  components: {
    Datepicker,
  },
  setup() {
    const picked = ref(new Date());
    const store = useStore();

    const { leagues, getLeagues, clubs, matches, getClubs, getMatchesByDay } =
      store;

    const items = ref([
      {
        src: EPL,
      },
      {
        src: Laliga,
      },
      {
        src: SerieA,
      },
    ]);

    const defaultURL =
      "https://image.shutterstock.com/z/stock-vector-image-icon-in-trendy-flat-style-isolated-on-white-background-award-symbol-for-your-web-site-design-643080895.jpg";

    
    const changeTab = async(leagueId) => {
        await getClubs(leagueId)
    }
    const loadData = async () => {
      await getLeagues();

      if (leagues.value.length > 0) {
        await getClubs(leagues.value[0].id);
      }
      await getMatchesByDay(picked.value);
    };

    onMounted(() => {
      loadData();
    });
    
    return {
      picked,
      leagues,
      clubs,
      items,
      matches,
      getMatchesByDay,
      defaultURL,
      changeTab
    };
  },
};
</script>

<style scoped>
.row {
  border: black 1px solid;

  margin-bottom: 5px;
  margin-top: 10px;
}

.background {
  background-color: lightgreen;
}

.colorrank {
  background-color: rgb(87, 168, 87);
  margin-bottom: 5px;
}

.clubranking {
  width: 95%;
  margin: 7px;
  max-height: 450px;
  overflow: auto;
}

.container {
  border: black 1px solid;
  height: 120px;
  display: flex;
  justify-content: space-around;
  border-radius: 10px;
  margin-top: 15px;
  margin-bottom: 15px;
}
.border {
  border: black 1px solid;

  height: 120px;
  margin-top: 10px;
  margin-bottom: 10px;
  border-radius: 10px;
}
.borderRow {
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: 10px;
  margin-right: 10px;
}
.borderCol {
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: 10px;
  margin-right: 10px;
  font-size: 32px;
  font-weight: bold;
}
.score {
  text-align: center;
  align-self: center;
  font-size: 32px;
  font-weight: bold;
}
</style>