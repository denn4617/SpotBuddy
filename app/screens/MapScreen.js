import React, { useEffect, useState } from "react";
import MapView from "react-native-maps";
import { Location, Permissions } from "expo";
import { View, SafeAreaView, StyleSheet, Dimensions, Button, Alert, TouchableOpacity, Text } from "react-native";
import axios from "axios";
import ActionButton from 'react-native-circular-action-menu';
import { Ionicons } from "@expo/vector-icons";
import { Component } from "react";



const MapScreen = () => {
  const [markers, setMarkers] = useState([])
  const [latitude, setLatitude] = useState(57.050528)
  const [longitude, setLongitude] = useState(9.912972)

  getSpots = async () => {
    try {
      await axios.get("http://172.20.10.7:5000/api/spots")
        .then(response => {
          setMarkers(response.data);
          console.log(response.data);
          console.log("This is the current state: " + markers[0].spot_id);
        })
        .catch(error => {
          console.log('Error fetching and parsing data', error);
        });
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    getSpots();
  }, [])



  return (
    <View style={{ flex: 1, alignItems: "center", justifyContent: "flex-end" }}>
      <MapView
        style={styles.map}
        showsUserLocation={true}
        initialRegion={{
          latitude: latitude,
          longitude: longitude,
          latitudeDelta: 0.0462,
          longitudeDelta: 0.0261,
        }}>

        {markers.map(marker => {
          return (
            <MapView.Marker
              key={marker.spot_id}
              coordinate={{ latitude: Number(marker.latitude), longitude: Number(marker.longitude) }}
            />
          )
        })}
      </MapView>

      <SafeAreaView //overlay button for adding new spots
        style={styles.overlay}
      >
        <ActionButton buttonColor="rgba(231,76,60,1)">
          <ActionButton.Item buttonColor='#9b59b6' title="New Task" onPress={() => console.log("create tapped!")}>
            <Ionicons name="create" style={styles.actionButtonIcon} />
          </ActionButton.Item>
          <ActionButton.Item buttonColor='#3498db' title="Notifications" onPress={() => console.log("notifications tapped!")}>
            <Ionicons name="notifications" style={styles.actionButtonIcon} />
          </ActionButton.Item>
          <ActionButton.Item buttonColor='#1abc9c' title="All Tasks" onPress={() => console.log("sad tapped!")}>
            <Ionicons name="sad" style={styles.actionButtonIcon} />
          </ActionButton.Item>
        </ActionButton>
      </SafeAreaView>
    </View>
  );
};
export default MapScreen;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
  map: {
    width: Dimensions.get("window").width,
    height: Dimensions.get("window").height,
  },
  overlay: {
    position: 'absolute',
    bottom: '4%',
    

  },
  appButtonContainer: {
    elevation: 8,
    // backgroundColor: "#009688",
    backgroundColor: "green",
    borderRadius: 10,
    paddingVertical: 10,
    paddingHorizontal: 12
  },
  appButtonText: {
    fontSize: 18,
    color: "#fff",
    fontWeight: "bold",
    alignSelf: "center",
    textTransform: "uppercase"
  },
  actionButtonIcon: {
    fontSize: 20,
    height: 22,
    color: 'white',
  },
});

