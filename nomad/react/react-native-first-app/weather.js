import React, {Component} from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { LinearGradient } from 'expo';
import { MaterialCommunityIcons } from "@expo/vector-icons";
import PropTypes from 'prop-types';

const WeatherCases = {
    Rain: {
        colors:["#00C6FB", "#005BEA"],
        title: "Raining",
        subtitle: "For more info look outside",
        icon: 'weather-pouring'
    },
    Clear: {
        colors:["#FEF253", "#FF7300"],
        title: "Sunny",
        subtitle: "For more info look outside",
        icon: 'weather-sunny'
    },
    Thunderstorm: {
        colors:["#00ECBC", "#007ADF"],
        title: "Thunderstorm",
        subtitle: "For more info look outside",
        icon: 'weather-lightning'
    },
    Clouds: {
        colors:["#D7D2CC", "#304352"],
        title: "Clouds",
        subtitle: "For more info look outside",
        icon: 'weather-cloudy'
    },
    Snow: {
        colors:["#7DE2FC", "#8986E5"],
        title: "Snow",
        subtitle: "For more info look outside",
        icon: 'weather-snowy'
    },
    Drizzle: {
        colors:["#89F7FE", "#66A6FF"],
        title: "Drizzle",
        subtitle: "For more info look outside",
        icon: 'weather-hail'
    },
    Haze: {
        colors:["#D7D2CC", "#304352"],
        title: "Haze",
        subtitle: "For more info look outside",
        icon: 'weather-fog'
    },
    Mist: {
        colors:["#D7D2CC", "#304352"],
        title: "Mist",
        subtitle: "For more info look outside",
        icon: 'weather-fog'
    }
}

function Weather({temp, weatherName}) {
    console.log(weatherName)
    return (
        <LinearGradient 
            colors={WeatherCases[weatherName].colors} 
            style={styles.container} 
        >
            <View style={styles.upper}>
                <MaterialCommunityIcons color="white" size={144} name={WeatherCases[weatherName].icon} />
                <Text style={styles.temp}>{temp}°C</Text>
            </View>
            <View style={styles.lower}>
                <Text style={styles.title}>{WeatherCases[weatherName].title}</Text>
                <Text style={styles.subtitle}>{WeatherCases[weatherName].subtitle}</Text>
            </View>
        </LinearGradient>
    );
}

Weather.propTypes = {
    temp: PropTypes.number.isRequired,
    weatherName: PropTypes.string.isRequired
}

export default Weather;

const styles = StyleSheet.create({
    container: {
        flex:1
    },
    upper: {
        flex: 1,
        alignItems:"center",
        justifyContent:"center",
        backgroundColor: "transparent"
    },
    temp: {
        fontSize: 48,
        backgroundColor: "transparent",
        color: "white",
        marginTop: 10
    },
    lower: {
        flex: 1,
        alignItems:"flex-start",
        justifyContent: 'flex-end',
        paddingLeft: 25
    },
    title: {
        fontSize: 38,
        backgroundColor: "transparent",
        color: "white",
        marginBottom: 10,
        fontWeight: '300'
    },
    subtitle: {
        fontSize: 24,
        backgroundColor: "transparent",
        color: "white",
        marginBottom: 24
    }
})