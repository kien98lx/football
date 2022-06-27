<template>
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
</template>

<script>

export default {
  setup () {
    return {}
  }
}
</script>
