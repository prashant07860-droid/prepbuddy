import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  ActivityIndicator,
  Dimensions,
} from 'react-native';
import { useRouter } from 'expo-router';
import { useQuery } from '@tanstack/react-query';
import { SafeAreaView } from 'react-native-safe-area-context';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { BarChart, LineChart, PieChart } from 'react-native-gifted-charts';
import { fetchAnalytics, fetchAttempts, fetchSubjects } from '../src/api';

const { width } = Dimensions.get('window');

export default function DashboardScreen() {
  const router = useRouter();

  const { data: analytics, isLoading: analyticsLoading } = useQuery({
    queryKey: ['analytics'],
    queryFn: fetchAnalytics,
  });

  const { data: subjects } = useQuery({
    queryKey: ['subjects'],
    queryFn: fetchSubjects,
  });

  const { data: recentAttempts } = useQuery({
    queryKey: ['recentAttempts'],
    queryFn: () => fetchAttempts(),
  });

  if (analyticsLoading) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color="#3B82F6" />
          <Text style={styles.loadingText}>Loading analytics...</Text>
        </View>
      </SafeAreaView>
    );
  }

  const subjectMap = subjects?.reduce((acc, s) => ({ ...acc, [s.id]: s }), {} as Record<string, any>) || {};

  // Prepare chart data
  const pieData = analytics?.subject_performance?.slice(0, 5).map((sp, index) => ({
    value: sp.attempts,
    color: ['#3B82F6', '#22C55E', '#F59E0B', '#EF4444', '#8B5CF6'][index],
    text: sp.subject_name.substring(0, 8),
  })) || [];

  const barData = analytics?.subject_performance?.map((sp) => ({
    value: sp.accuracy,
    label: sp.subject_name.substring(0, 4),
    frontColor: sp.accuracy >= 70 ? '#22C55E' : sp.accuracy >= 40 ? '#F59E0B' : '#EF4444',
  })) || [];

  const lineData = analytics?.recent_scores?.slice(0, 10).reverse().map((rs) => ({
    value: rs.score,
  })) || [];

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <TouchableOpacity
          style={styles.backButton}
          onPress={() => router.back()}
        >
          <MaterialCommunityIcons name="arrow-left" size={24} color="#F8FAFC" />
        </TouchableOpacity>
        <Text style={styles.headerTitle}>Performance Dashboard</Text>
        <View style={styles.placeholder} />
      </View>

      <ScrollView
        style={styles.scrollView}
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
      >
        {/* Overview Cards */}
        <View style={styles.overviewGrid}>
          <View style={styles.overviewCard}>
            <MaterialCommunityIcons name="clipboard-check" size={28} color="#3B82F6" />
            <Text style={styles.overviewValue}>{analytics?.total_attempts || 0}</Text>
            <Text style={styles.overviewLabel}>Total Attempts</Text>
          </View>
          <View style={styles.overviewCard}>
            <MaterialCommunityIcons name="percent" size={28} color="#22C55E" />
            <Text style={styles.overviewValue}>{analytics?.overall_accuracy || 0}%</Text>
            <Text style={styles.overviewLabel}>Accuracy</Text>
          </View>
          <View style={styles.overviewCard}>
            <MaterialCommunityIcons name="trophy" size={28} color="#F59E0B" />
            <Text style={styles.overviewValue}>{analytics?.best_score || 0}%</Text>
            <Text style={styles.overviewLabel}>Best Score</Text>
          </View>
          <View style={styles.overviewCard}>
            <MaterialCommunityIcons name="chart-line" size={28} color="#8B5CF6" />
            <Text style={styles.overviewValue}>{analytics?.average_score || 0}%</Text>
            <Text style={styles.overviewLabel}>Average</Text>
          </View>
        </View>

        {/* Progress Trend */}
        {lineData.length > 1 && (
          <View style={styles.chartCard}>
            <Text style={styles.chartTitle}>Score Trend</Text>
            <Text style={styles.chartSubtitle}>Your last {lineData.length} attempts</Text>
            <View style={styles.chartContainer}>
              <LineChart
                data={lineData}
                width={width - 80}
                height={150}
                spacing={(width - 100) / Math.max(lineData.length - 1, 1)}
                color="#3B82F6"
                thickness={3}
                dataPointsColor="#3B82F6"
                dataPointsRadius={5}
                hideRules
                yAxisColor="#334155"
                xAxisColor="#334155"
                yAxisTextStyle={{ color: '#64748B', fontSize: 10 }}
                maxValue={100}
                noOfSections={4}
                areaChart
                startFillColor="#3B82F6"
                endFillColor="#0F172A"
                startOpacity={0.4}
                endOpacity={0}
                curved
              />
            </View>
          </View>
        )}

        {/* Subject Performance */}
        {barData.length > 0 && (
          <View style={styles.chartCard}>
            <Text style={styles.chartTitle}>Subject-wise Accuracy</Text>
            <Text style={styles.chartSubtitle}>Percentage accuracy per subject</Text>
            <View style={styles.chartContainer}>
              <BarChart
                data={barData}
                width={width - 80}
                height={180}
                barWidth={22}
                spacing={12}
                hideRules
                yAxisColor="#334155"
                xAxisColor="#334155"
                yAxisTextStyle={{ color: '#64748B', fontSize: 10 }}
                xAxisLabelTextStyle={{ color: '#64748B', fontSize: 9 }}
                maxValue={100}
                noOfSections={4}
                barBorderRadius={4}
                isAnimated
              />
            </View>
          </View>
        )}

        {/* Attempts Distribution */}
        {pieData.length > 0 && (
          <View style={styles.chartCard}>
            <Text style={styles.chartTitle}>Practice Distribution</Text>
            <Text style={styles.chartSubtitle}>Attempts across subjects</Text>
            <View style={styles.pieContainer}>
              <PieChart
                data={pieData}
                donut
                radius={80}
                innerRadius={50}
                centerLabelComponent={() => (
                  <View style={styles.pieCenter}>
                    <Text style={styles.pieCenterValue}>{analytics?.total_attempts}</Text>
                    <Text style={styles.pieCenterLabel}>Total</Text>
                  </View>
                )}
              />
              <View style={styles.pieLegend}>
                {pieData.map((item, index) => (
                  <View key={index} style={styles.legendItem}>
                    <View style={[styles.legendDot, { backgroundColor: item.color }]} />
                    <Text style={styles.legendText}>{item.text}</Text>
                    <Text style={styles.legendValue}>{item.value}</Text>
                  </View>
                ))}
              </View>
            </View>
          </View>
        )}

        {/* Subject Performance Table */}
        <View style={styles.tableCard}>
          <Text style={styles.chartTitle}>Detailed Performance</Text>
          <View style={styles.tableHeader}>
            <Text style={[styles.tableHeaderText, { flex: 2 }]}>Subject</Text>
            <Text style={styles.tableHeaderText}>Attempts</Text>
            <Text style={styles.tableHeaderText}>Accuracy</Text>
            <Text style={styles.tableHeaderText}>Best</Text>
          </View>
          {analytics?.subject_performance?.map((sp, index) => (
            <View key={sp.subject_id} style={styles.tableRow}>
              <Text style={[styles.tableCell, { flex: 2 }]} numberOfLines={1}>
                {sp.subject_name}
              </Text>
              <Text style={styles.tableCell}>{sp.attempts}</Text>
              <Text style={[
                styles.tableCell,
                { color: sp.accuracy >= 70 ? '#22C55E' : sp.accuracy >= 40 ? '#F59E0B' : '#EF4444' }
              ]}>
                {sp.accuracy}%
              </Text>
              <Text style={styles.tableCell}>{sp.best_score}%</Text>
            </View>
          ))}
        </View>

        {/* Recent Attempts */}
        {recentAttempts && recentAttempts.length > 0 && (
          <View style={styles.recentCard}>
            <Text style={styles.chartTitle}>Recent Attempts</Text>
            {recentAttempts.slice(0, 5).map((attempt, index) => {
              const subject = subjectMap[attempt.subject_id];
              return (
                <TouchableOpacity
                  key={attempt.id}
                  style={styles.attemptItem}
                  onPress={() => router.push(`/results/${attempt.id}`)}
                >
                  <View style={styles.attemptLeft}>
                    <Text style={styles.attemptSubject} numberOfLines={1}>
                      {subject?.name || 'Unknown'}
                    </Text>
                    <Text style={styles.attemptDate}>
                      {new Date(attempt.created_at).toLocaleDateString()}
                    </Text>
                  </View>
                  <View style={styles.attemptRight}>
                    <Text style={[
                      styles.attemptScore,
                      {
                        color: attempt.score_percentage >= 70
                          ? '#22C55E'
                          : attempt.score_percentage >= 40
                          ? '#F59E0B'
                          : '#EF4444'
                      }
                    ]}>
                      {attempt.score_percentage}%
                    </Text>
                    <MaterialCommunityIcons name="chevron-right" size={20} color="#64748B" />
                  </View>
                </TouchableOpacity>
              );
            })}
          </View>
        )}

        {/* Empty State */}
        {(!analytics || analytics.total_attempts === 0) && (
          <View style={styles.emptyState}>
            <MaterialCommunityIcons name="chart-box-outline" size={64} color="#475569" />
            <Text style={styles.emptyTitle}>No Data Yet</Text>
            <Text style={styles.emptyText}>
              Complete some practice papers to see your performance analytics here.
            </Text>
            <TouchableOpacity
              style={styles.startButton}
              onPress={() => router.replace('/')}
            >
              <Text style={styles.startButtonText}>Start Practicing</Text>
            </TouchableOpacity>
          </View>
        )}

        <View style={styles.bottomPadding} />
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0F172A',
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  loadingText: {
    marginTop: 12,
    fontSize: 16,
    color: '#94A3B8',
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 16,
    paddingVertical: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#1E293B',
  },
  backButton: {
    width: 40,
    height: 40,
    borderRadius: 10,
    backgroundColor: '#1E293B',
    justifyContent: 'center',
    alignItems: 'center',
  },
  headerTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: '#F8FAFC',
  },
  placeholder: {
    width: 40,
  },
  scrollView: {
    flex: 1,
  },
  scrollContent: {
    padding: 16,
  },
  overviewGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 12,
    marginBottom: 20,
  },
  overviewCard: {
    flex: 1,
    minWidth: '45%',
    backgroundColor: '#1E293B',
    borderRadius: 16,
    padding: 16,
    alignItems: 'center',
  },
  overviewValue: {
    fontSize: 24,
    fontWeight: '700',
    color: '#F8FAFC',
    marginTop: 8,
  },
  overviewLabel: {
    fontSize: 12,
    color: '#64748B',
    marginTop: 4,
  },
  chartCard: {
    backgroundColor: '#1E293B',
    borderRadius: 16,
    padding: 20,
    marginBottom: 16,
  },
  chartTitle: {
    fontSize: 16,
    fontWeight: '600',
    color: '#F8FAFC',
    marginBottom: 4,
  },
  chartSubtitle: {
    fontSize: 12,
    color: '#64748B',
    marginBottom: 16,
  },
  chartContainer: {
    alignItems: 'center',
  },
  pieContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-around',
  },
  pieCenter: {
    alignItems: 'center',
  },
  pieCenterValue: {
    fontSize: 20,
    fontWeight: '700',
    color: '#F8FAFC',
  },
  pieCenterLabel: {
    fontSize: 10,
    color: '#64748B',
  },
  pieLegend: {
    gap: 8,
  },
  legendItem: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  legendDot: {
    width: 10,
    height: 10,
    borderRadius: 5,
  },
  legendText: {
    fontSize: 12,
    color: '#94A3B8',
    flex: 1,
  },
  legendValue: {
    fontSize: 12,
    fontWeight: '600',
    color: '#F8FAFC',
  },
  tableCard: {
    backgroundColor: '#1E293B',
    borderRadius: 16,
    padding: 20,
    marginBottom: 16,
  },
  tableHeader: {
    flexDirection: 'row',
    paddingVertical: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#334155',
    marginTop: 8,
  },
  tableHeaderText: {
    flex: 1,
    fontSize: 11,
    fontWeight: '600',
    color: '#64748B',
    textAlign: 'center',
  },
  tableRow: {
    flexDirection: 'row',
    paddingVertical: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#1E293B',
  },
  tableCell: {
    flex: 1,
    fontSize: 13,
    color: '#F8FAFC',
    textAlign: 'center',
  },
  recentCard: {
    backgroundColor: '#1E293B',
    borderRadius: 16,
    padding: 20,
    marginBottom: 16,
  },
  attemptItem: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingVertical: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#334155',
  },
  attemptLeft: {
    flex: 1,
  },
  attemptSubject: {
    fontSize: 14,
    fontWeight: '500',
    color: '#F8FAFC',
    marginBottom: 2,
  },
  attemptDate: {
    fontSize: 12,
    color: '#64748B',
  },
  attemptRight: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  attemptScore: {
    fontSize: 16,
    fontWeight: '700',
  },
  emptyState: {
    alignItems: 'center',
    paddingVertical: 40,
  },
  emptyTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: '#F8FAFC',
    marginTop: 16,
  },
  emptyText: {
    fontSize: 14,
    color: '#64748B',
    textAlign: 'center',
    marginTop: 8,
    marginHorizontal: 40,
  },
  startButton: {
    marginTop: 20,
    paddingHorizontal: 24,
    paddingVertical: 12,
    backgroundColor: '#3B82F6',
    borderRadius: 10,
  },
  startButtonText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#FFFFFF',
  },
  bottomPadding: {
    height: 20,
  },
});
