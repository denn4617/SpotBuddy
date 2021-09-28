import React from "react";
import MapView from "react-native-maps";
import { Location, Permissions } from "expo";
import { View, Text, StyleSheet, Dimensions, TouchableOpacity } from "react-native";
import { Component } from "react";


const MapScreen = () => {

  getSpots = () => {
    try {
      axios.get("localhost:5000/api/spots")
        .then(response => {
          this.setState({ markers: response });
          console.log(this.state.markers);
        })
        .catch(error => {
          console.log('Error fetching and parsing data', error);
        });
    } catch (error) {
      console.log(error);
    }
  }

  return (
    <View style={{ flex: 1, alignItems: "center", justifyContent: "center" }}>
      <MapView
        style={styles.map}
        showsUserLocation={true}
        /*initialRegion={{
          latitude: this.state.latitude,
          longitude: this.state.longitude,
          latitudeDelta: 0.0462,
          longitudeDelta: 0.0261,
        }}*/>

        {this.state.markers.map(marker => (
          <Marker
            coordinate={{ latitude: marker.member.latitude, longitude: marker.member.longitude }}
          />
        ))}

        <MapView.Marker
          key={2}
          coordinate={{ latitude: 57.035017, longitude: 9.946407 }}
          title={"test title"}
          description={"test descrip"}
        />



      </MapView>

      <TouchableOpacity style={styles.overlay}>
        <Text style={styles.text}>Touchable Opacity</Text>
      </TouchableOpacity>
      <Text>Map Screen</Text>
    </View>
  );
};
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
    bottom: 50,
    backgroundColor: 'rgba(255, 255, 255, 1)',
  },
});
export default MapScreen;
