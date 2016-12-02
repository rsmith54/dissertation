#include "TGraph.h"

// macro for making the regionYieldErrorSystematic plot

void regionYieldErrorSystematic(){
  vector<double> verror; // error (%)
  vector<double> vyield; // SR yield (N events)

  vyield.push_back(206.91);
  verror.push_back(7.71);

  vyield.push_back(142.29);
  verror.push_back(7.39);

  vyield.push_back(51.18);
  verror.push_back(9.08);

  vyield.push_back(39.08);
  verror.push_back(8.18);

  vyield.push_back(26.70);
  verror.push_back(8.62);

  vyield.push_back(17.58);
  verror.push_back(8.67);

  vyield.push_back(55.69);
  verror.push_back(9.16);

  vyield.push_back(24.58);
  verror.push_back(8.97);

  vyield.push_back(14.27);
  verror.push_back(12.02);

  vyield.push_back(4.14);
  verror.push_back(14.82);

  vyield.push_back(2.79);
  verror.push_back(19.73);

  vyield.push_back(0.79);
  verror.push_back(33.55);

  vyield.push_back(7.58);
  verror.push_back(14.37);

  vyield.push_back(31.00);
  verror.push_back(10.61);

  vyield.push_back(55.88);
  verror.push_back(10.75);

  vyield.push_back(5.14);
  verror.push_back(20.02);

  vyield.push_back(3.2);
  verror.push_back(18.67);

  int N = vyield.size();
  double yield[N];
  double error[N];

  for(int i = 0; i < N; i++){
    yield[i] = vyield[i];
    error[i] = verror[i];
  }
  
  TGraph* gr = new TGraph(N, yield, error);
  gr->Draw("AP");

  
}

