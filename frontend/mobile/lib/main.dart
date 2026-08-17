import 'package:flutter/material.dart';

void main() {
  runApp(const PhysicsPortalApp());
}

class PhysicsPortalApp extends StatelessWidget {
  const PhysicsPortalApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Physics Department Portal',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.indigo),
        useMaterial3: true,
      ),
      home: const PortalHomePage(),
    );
  }
}

class PortalHomePage extends StatelessWidget {
  const PortalHomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Physics Department Portal'),
      ),
      body: ListView(
        padding: const EdgeInsets.all(20),
        children: const [
          Text(
            'Govt. Edward College, Pabna',
            style: TextStyle(fontWeight: FontWeight.bold),
          ),
          SizedBox(height: 8),
          Text(
            'Mobile application foundation. Authentication and the student dashboard will be connected to the FastAPI backend next.',
          ),
          SizedBox(height: 28),
          _FeatureCard(
            icon: Icons.bar_chart,
            title: 'Attendance',
            description: 'View course attendance.',
          ),
          _FeatureCard(
            icon: Icons.assignment,
            title: 'Assignments',
            description: 'View and submit assignments.',
          ),
          _FeatureCard(
            icon: Icons.event,
            title: 'Events',
            description: 'See upcoming department events.',
          ),
          _FeatureCard(
            icon: Icons.campaign,
            title: 'Announcements',
            description: 'Read department announcements.',
          ),
        ],
      ),
    );
  }
}

class _FeatureCard extends StatelessWidget {
  final IconData icon;
  final String title;
  final String description;

  const _FeatureCard({
    required this.icon,
    required this.title,
    required this.description,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      child: ListTile(
        leading: Icon(icon),
        title: Text(title),
        subtitle: Text(description),
      ),
    );
  }
}
