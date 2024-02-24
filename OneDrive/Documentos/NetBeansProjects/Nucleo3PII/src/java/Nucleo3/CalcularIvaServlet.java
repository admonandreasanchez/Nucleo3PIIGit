package Nucleo3;

import java.io.IOException;
import java.io.PrintWriter;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@WebServlet("/calcularivaServlet")

public class CalcularIvaServlet extends HttpServlet {

    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            String producto = request.getParameter("producto");
            String costoString = request.getParameter("costo");
            
            // Validar que el costo ingresado sea un número
            double costo;
            try {
                costo = Double.parseDouble(costoString);
            } catch (NumberFormatException e) {
                out.println("<!DOCTYPE html>");
                out.println("<html>");
                out.println("<head>");
                out.println("<title>Error</title>");
                out.println("</head>");
                out.println("<body>");
                out.println("<h2>Error: El costo ingresado no es válido. Por favor ingrese un número válido.</h2>");
                out.println("</body>");
                out.println("</html>");
                return; // Terminar la ejecución del servlet
            }
            
            // Calcular el IVA (por ejemplo, 19%)
            double iva = costo * 0.19;
            double costoFinal = costo + iva;
            
            // Mostrar la respuesta en una página web
            out.println("<!DOCTYPE html>");
            out.println("<html>");
            out.println("<head>");
            out.println("<title>Resultado del Cálculo de IVA</title>");
            out.println("</head>");
            out.println("<body>");
            out.println("<h2>Resultado del Cálculo de IVA</h2>");
            out.println("<p>Producto: " + producto + "</p>");
            out.println("<p>Costo del Producto: $" + costo + "</p>");
            out.println("<p>IVA: $" + iva + "</p>");
            out.println("<p>Costo Final (con IVA): $" + costoFinal + "</p>");
            out.println("</body>");
            out.println("</html>");
        }
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    @Override
    public String getServletInfo() {
        return "Short description";
    }
}