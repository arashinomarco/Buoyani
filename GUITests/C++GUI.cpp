#include <QApplication>
#include <QPushButton>
#include <QIcon>
#include <QProcess>
#include <QMessageBox>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    QWidget window;
    window.setWindowTitle("Desktop Application");
    window.setWindowIcon(QIcon(":/icon.png"));
    QLabel *label = new QLabel(&window);
    label->setText("Desktop Application");
    label->setFont(QFont("Arial", 14));
    label->setAlignment(Qt::AlignCenter);

    QPushButton *button = new QPushButton("Run Script", &window);
    QObject::connect(button, &QPushButton::clicked, [&](){
        QProcess process;
        process.start("python", QStringList() << "samplescript.py");
        process.waitForFinished(-1);
        if (process.exitCode() != 0) {
            QMessageBox::critical(&window, "Error", "Failed to execute the Python script");
        }
    });

    QVBoxLayout *layout = new QVBoxLayout(&window);
    layout->addWidget(label);
    layout->addWidget(button);
    window.setLayout(layout);

    window.show();

    return app.exec();
}
